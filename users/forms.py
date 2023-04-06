from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from jobs.models import Company

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        

class CompanyCreationForm(ModelForm):

    class Meta:
        model = Company
        exclude = ['user']