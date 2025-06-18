from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('submit_form/',views.my_form,name='submit_form'),
    path('django_form/',views.DjangoForm,name="django_form"),
    
]
