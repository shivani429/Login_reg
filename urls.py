from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from demoapp.views import *
from django.conf.urls import url

urlpatterns = [

    path("h",views.home,name='home'),
    path("reg", views.reg,name='reg'),
    path("log",views.login,name='login')
        
  
]
