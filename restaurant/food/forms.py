from django import forms
from django.db.models import fields
from .models import program

class contactform(forms.ModelForm):
    class Meta:
        model = program
        fields =['name']