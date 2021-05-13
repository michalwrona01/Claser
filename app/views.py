from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.utils import timezone



def home(request):
    person = Person.objects.get(id=1)
    classroom = person.classroom
    subjects = Subject.objects.filter(classroom__name=classroom.name)
    marks = Mark.objects.filter(students__name=person.name)



    context = {
                'user' : person,
                'subjects' : subjects,
                'classroom' : classroom,
                'marks' : marks,
                }


    return render(request, 'app/home.html', context)

def subject_panel(request, pk):
    classroom = Person.objects.get(id=1).classroom
    subject = Subject.objects.get(id=pk)
    posts = Post.objects.filter(classroom=classroom).filter(subject=subject)

    context = {'posts' : posts,
                'subject' : subject,
                'classroom' : classroom,
                }


    return render(request, 'app/subject_panel.html', context)