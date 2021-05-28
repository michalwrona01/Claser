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

class MarkAddForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'

        widgets = {
            'mark_number' : forms.Select(attrs={'class' : 'form-control', 'label' : 'Mark'}),
            'description' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Description'}),
            'students' : forms.CheckboxSelectMultiple(attrs={'class' : 'form-check-input', 'type' : 'checkbox',}),
            'classroom' : forms.HiddenInput(),
            'subject' : forms.HiddenInput(),
            'created_person' : forms.HiddenInput(),
            'date_created' : forms.HiddenInput(),
        }

    def __init__(self, classroom_pk, *args, **kwargs):
        super(MarkAddForm, self).__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.filter(classroom_id=classroom_pk)
    


    

    

