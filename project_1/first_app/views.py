from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("This is course app")

def about(request):
    return HttpResponse("This is about page")    

def home(request):
    return HttpResponse("this is first app/home page")
    