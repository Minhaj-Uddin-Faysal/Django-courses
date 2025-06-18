from django.shortcuts import render,redirect,get_object_or_404
from .forms import BookForm,CommentPost
from .models import Book,Review
# Create your views here.
def home(request):
    books=Book.objects.all()
    return render(request,'home.html',{'books':books})
    
def add_book(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            author=form.cleaned_data['author']
            published_date=form.cleaned_data['published_date']
            pages=form.cleaned_data['pages']
            Book.objects.create(title=title,author=author,published_date=published_date,pages=pages)
            return redirect('home')
    else:
        form=BookForm()
    return render(request,'add_book.html',{'form':form})

    
def deleteBook(request,id):
    book=get_object_or_404(Book,id=id)
    book.delete()
    return redirect('home')


def search_book(request):
    query=request.GET.get('q',' ')
    if query:
        results=Book.objects.filter(title__icontains=query)
        if len(results)==0:
            results=Book.objects.all()

    else:
        results=Book.objects.all()    

    return render(request,'home.html',{'books':results,'query':query})


def reviews(request,title):
    if request.method=="POST":
        comment=Review.objects.filter(title=title)
        form=CommentPost()
    return render(request,'post.html',{'form':form,'comment':comment,'title':title})
    

def commentpost(request,title):
    if request.method=="POST":
        form=CommentPost(request.POST)
        if form.is_valid():
            text=form.cleaned_data['comment']
            Review.objects.create(title=title,comment=text)
            comment=Review.objects.filter(title=title)
            form=CommentPost()
    return render(request,'post.html',{'form':form,'comment':comment,'title':title})
    
