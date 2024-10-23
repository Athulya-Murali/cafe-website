from django.shortcuts import render
from shop.models import *
from . models import *

# Create your views here.
def success(request):
    return render(request,'success.html')