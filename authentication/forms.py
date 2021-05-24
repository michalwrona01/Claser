from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields, widgets
from app.models import Student, Teacher, Director


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control', 'id' : 'floatingInput', 'placeholder' : 'janek123'}),
            'first_name': forms.TextInput(attrs={'class' : 'form-control', 'id' : 'floatingInput', 'placeholder' : 'Jan'}),
            'last_name': forms.TextInput(attrs={'class' : 'form-control', 'id' : 'floatingInput', 'placeholder' : 'Kowalski'}),
            'email': forms.EmailInput(attrs={'type' : 'email', 'class' : 'form-control', 'id' : 'floatingInput', 'placeholder' : 'name@example.com'}),
            'password1' : forms.PasswordInput(attrs={'class' : 'form-control', 'id' : 'floatingPassword', 'placeholder' : 'Password'}),
            'password2' : forms.PasswordInput(attrs={'class' : 'form-control', 'id' : 'floatingPassword', 'placeholder' : 'Password'}),
        }


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['is_student']

        widgets = {
            'classroom' : forms.Select(attrs={'class' : 'form-select'}),
            'phone_number' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '123456789'}),
            'personal_identity_number' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'PESEL'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Warszawa ul. Mazowiecka 121'}),
            'user' : forms.HiddenInput()
        }

class TeacherCreationForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude  = ['is_teacher']

        widgets = {
            'classrooms' : forms.CheckboxSelectMultiple(attrs={'class' : 'form-check-input', 'type' : 'checkbox'}),
            'subjects' : forms.CheckboxSelectMultiple(attrs={'class' : 'form-check-input', 'type' : 'checkbox'}),
            'phone_number' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '123456789'}),
            'personal_identity_number' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'PESEL'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Warszawa ul. Mazowiecka 121'}),
            'user' : forms.HiddenInput()
        }

class DirectorCreationForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
        exclude  = ['is_director']

        widgets = {
            'phone_number' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : '123456789'}),
            'personal_identity_number' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'PESEL'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Warszawa ul. Mazowiecka 121'}),
            'user' : forms.HiddenInput()
        }
