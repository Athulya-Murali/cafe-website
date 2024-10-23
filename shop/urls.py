from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='hm'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('signup/',views.signup,name='signup'),
    path('login/', views.login, name='login'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:c_slug>/', views.gallery_category, name='gallery_category'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodDetails,name='details'),
    path('search',views.searching,name='search'),
]
