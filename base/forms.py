from django import forms
from django.forms import ModelForm
from .models import BaseUser

class UserForm(forms.ModelForm):
    class Meta:
        model = BaseUser
        fields = '__all__'