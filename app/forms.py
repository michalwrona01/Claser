from django import forms
from .models import *

class PostAddForm(forms.ModelForm):
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
