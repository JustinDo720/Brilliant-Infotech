from .models import * 
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'