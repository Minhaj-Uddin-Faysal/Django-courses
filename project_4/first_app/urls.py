from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('base/',views.base,name='base_page'),
    path('home/',views.homee,name='home_page'),

   
]
