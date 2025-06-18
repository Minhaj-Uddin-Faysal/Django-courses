from django.shortcuts import render
from .models import Teacher
# Create your views here.

def teacher(request):
    teachers=Teacher.objects.prefetch_related('courses').all()
    return render(request,'teacherinfo.html',{'teacher':teachers})
    