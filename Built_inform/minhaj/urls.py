from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('student_form/',views.studentform),
    path('password/',views.Passwordvalidation),
    
]