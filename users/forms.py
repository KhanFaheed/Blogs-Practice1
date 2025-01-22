from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User   #model to which this form is going to interact
        fields=['username','email','password1','password2']
        






