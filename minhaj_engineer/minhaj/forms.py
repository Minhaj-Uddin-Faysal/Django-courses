from django import forms

class BookForm(forms.Form):
    title=forms.CharField(max_length=100,label="Book Name")
    author=forms.CharField(
        max_length=100)
    
    published_date=forms.DateField(widget=forms.DateInput(attrs={
        'type':'date'
    }))
    
    pages=forms.IntegerField()



class CommentPost(forms.Form):
    comment=forms.CharField(widget=forms.Textarea)

