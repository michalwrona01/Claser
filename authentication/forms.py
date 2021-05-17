from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from app.models import Student, Teacher


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control', 'id' : 'floatingInput', 'placeholder' : 'janek123'}),
            'first_name': forms.TextInput(attrs={'class' : 'form-control', 'id' : 'floatingInput', 'placeholder' : 'Jan'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control', 'id' : 'floatingInput', 'placeholder' : 'Kowalski'}),
            'email': forms.EmailInput(attrs={'type' : 'email', 'class' : 'form-control', 'id' : 'floatingInput', 'placeholder' : 'name@example.com'}),
        }




