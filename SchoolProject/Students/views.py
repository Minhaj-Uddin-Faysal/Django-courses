from django.shortcuts import render
from .models import Students
# Create your views here.
def studentinfo(request):
    student=Students.objects.all()
    return render(request,'info.html',{'student':student})


    
    