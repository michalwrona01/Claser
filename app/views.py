from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
    homeworks = Homework.objects.filter(subject=subject)

    context = {'posts' : posts,
                'subject' : subject,
                'classroom' : classroom,
                'homeworks' : homeworks,
                }


    return render(request, 'app/subject_panel.html', context)

def dashboard(request):
    classroom = Person.objects.get(id=1).classroom
    context = {
        'classroom' : classroom,
    }
    
    
    return render(request, 'app/choice_classroom.html', context)

def classroom_panel(request, pk):
    classroom = Classroom.objects.get(id=pk)
    students = Person.objects.filter(classroom=classroom)

    context = {
        'classroom' : classroom,
        'students' : students,
    }

    return render(request, 'app/dashboard.html', context)
    
