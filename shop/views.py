from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from . models import product 
from django.http import HttpResponseBadRequest

# Create your views here.
def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = product.objects.filter(category=c_page,available=True).order_by('id')
    else:
        prodt = product.objects.all().filter(available=True).order_by('id')

        #paginator code start
    paginator = Paginator(prodt,3)
    try:
        page =int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        prodt = paginator.page(page)
    except(EmptyPage,InvalidPage):
        prodt = Paginator.page(paginator.num_pages)
    #paginator code ends
    
    cat = categ.objects.all()
    return render(request,'index.html',{'pr':prodt,'ct':cat})


def prodDetails(request,c_slug,product_slug):
    try:
        prod = product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product-detailpage.html',{'pr':prod})


def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'q':query,'pr':prod})


def gallery(request,c_slug=None):
    categories = categ.objects.all()
    if c_slug:
        selected_category = get_object_or_404(categ, slug=c_slug)
        products = product.objects.filter(category=selected_category, available=True)
    else:
        selected_category = None
    products = product.objects.filter(available=True)
    return render(request, 'gallery.html', {'categories': categories, 'pr': products})

def gallery_category(request, c_slug):
    category = get_object_or_404(categ, slug=c_slug)
    products = product.objects.filter(category=category, available=True)
    return render(request, 'gallery.html', {'selected_category': category, 'pr': products})


def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
