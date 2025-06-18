from django import forms

class contactform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
