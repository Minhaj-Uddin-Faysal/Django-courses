from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('first_app/',include("first_app.urls")),
    path('',views.index),
]
