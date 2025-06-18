from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        labels={
            'name':'student name',
            'roll':'Student Roll',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'btn-primary'}),
             'roll':forms.PasswordInput()
        }
        help_texts={
            'name':"Write your full text",
            
        }
        error_messages={
            'name':{
                'required':'Your name is required'
                }
        }