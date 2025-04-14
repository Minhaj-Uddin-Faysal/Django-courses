from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={'author':'Rahim','age':15,'lst':['Python','is','best'],
    'birthday':datetime.datetime.now(),'val':'','courses':[
        {
            'id':1,
            'name':'python',
            'fee':'1000',
        }
        ,
        {
            'id':2,
            'name':'Django',
            'fee':'2000',
        }
        ,
        {
            'id':3,
            'name':'Hero',
            'fee':'40000',
        }
    ]}
    return render(request,'home.html',d)
