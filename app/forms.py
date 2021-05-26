from django import forms
from django.db.models import fields
from .models import *

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'topic' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Topic'}),
            'text' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Text'}),
            'classroom' : forms.HiddenInput(),
            'subject' : forms.HiddenInput(),
            'created_person' : forms.HiddenInput(),
            'date_created' : forms.HiddenInput(),
        }

class HomeworkCreationForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = '__all__'

        widgets = {
            'task' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Task'}),
            'text' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Text'}),
            'deadline_date' : forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}),
            'classroom' : forms.HiddenInput(),
            'subject' : forms.HiddenInput(),
            'created_person' : forms.HiddenInput(),
            'date_created' : forms.HiddenInput(),
        }
