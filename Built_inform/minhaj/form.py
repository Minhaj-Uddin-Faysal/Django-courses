from django import forms
from django.core import validators

class MyForm(forms.Form):
    name=forms.CharField(label="Your Name",max_length=100,widget=forms.Textarea(attrs={'id':'text_area',
    'class':'1'}),initial='Text write ')
    file=forms.FileField()
    # email=forms.EmailField(label="Your Email")
    # age=forms.IntegerField(label="Age")
    # weight=forms.FloatField(label="Weight")
    # balance=forms.IntegerField(label="Balance")
    # check=forms.BooleanField()
    CHOICES=[  ('A', 'Apple'),
    ('B', 'Ball'),
    ('C', 'Cat'),]
    age=forms.CharField(widget=forms.NumberInput)
    BirthDate=forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment=forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    size=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    Box=forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple)    

class studentData(forms.Form):
    name=forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(10,message='Must be atleast than 10 char')])
    email=forms.CharField(widget=forms.EmailInput)
    age=forms.IntegerField(validators=[validators.MaxValueValidator(34),validators.
    MinValueValidator(24)])
    # def clean_name(self):
    #     valname=self.cleaned_data['name']
    #     if len(valname)<10:
    #         raise forms.ValidationError("Enter a name with at least 10 Charachters")
    #     return valname

        
class PasswordValidationProject(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data=super().clean()
        val_pass=self.cleaned_data['password']
        val_conform=self.cleaned_data['confirm_password']
        val_nam=self.cleaned_data['name']
        if val_pass!=val_conform:
            raise forms.ValidationError('password not correct')
        if len(val_nam)<15:
            raise froms.ValidationError('name is too lengthy')

            