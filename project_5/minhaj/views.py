from django.shortcuts import render,redirect
from . import models
from .forms import StudentForm
# Create your views here.

def home(request):
    student=models.Student.objects.all()
    print(student)
    return render(request,"home.html",{'data':student})
    
def delete_student(request,roll):
    std=models.Student.objects.get(pk=roll).delete()
    student=models.Student.objects.all()
    return render(request,"home.html",{'data':student})
    
def Modelform(request):
    std=StudentForm
    return render(request,'form.html',{'form':std})
