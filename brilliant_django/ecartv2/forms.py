from .models import *
from django import forms 

class EmployeeForm(forms.ModelForm):
    class meta:
        model = EmployeeModelV2
        fields = '__all__'



