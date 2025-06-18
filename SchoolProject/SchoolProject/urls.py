from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('auth/',include('account.urls')),
    path('student/',include('Students.urls')),
    path('teacher/',include('Teachers.urls')),
    path('profile/',include('user_profile.urls')),

    path('',views.firstpage,name='firstpage'),
]
