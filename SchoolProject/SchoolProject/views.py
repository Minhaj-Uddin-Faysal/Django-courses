from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def firstpage(request):
    return render(request,'firstpage.html')

    
    