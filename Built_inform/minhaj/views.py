from django.shortcuts import render
from .form import MyForm,studentData,PasswordValidationProject
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.method=='POST':
        form=MyForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            file=form.cleaned_data['file']
            with open('./minhaj/upload/'+file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            form=MyForm()
            return render(request,'form.html',{'form':form})
        else:
            form=MyForm()
            print(form.errors)
            print("Invalid")
            return render(request,'form.html',{'form':form})            
        
    else:
        form=MyForm()
        return render(request,'form.html',{'form':form})            
        

def studentform(request):
    if request.method=='POST':
        form=studentData(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form=studentData()
            
    else:
        form=studentData()

    return render(request,'form.html',{'form':form})            
             
def Passwordvalidation(request):
    if request.method=='POST':
        form=PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form=PasswordValidationProject()
            
    else:
        form=PasswordValidationProject()

    return render(request,'form.html',{'form':form})            
 