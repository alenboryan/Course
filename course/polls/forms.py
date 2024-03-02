from django import forms
from .models import Course
from django.forms import TextInput

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'rate', 'count']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name Course'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "count": forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            "count": forms.NumberInput(attrs={
                'class': 'form-control'
            })
        }


    




