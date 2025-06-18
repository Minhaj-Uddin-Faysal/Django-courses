from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method=='category':
        category_form=forms.CtegoryForm(request.category)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form=forms.CategoryForm()        
    return render(request,'add_category.html',{'form':category_form})
    