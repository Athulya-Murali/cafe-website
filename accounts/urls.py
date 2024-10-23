from django.urls import path, include
from .views import success
from . import views


urlpatterns = [
    path('success',success,name="success")

]