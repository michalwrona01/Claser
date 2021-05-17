from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def home(request):
    student = Student.objects.get(id=1)
    classroom = student.classroom
    subjects = Subject.objects.filter(classroom__name=classroom.name)
    marks = Mark.objects.filter(students__id=student.id)


    context = {
                'student' : student,
                'subjects' : subjects,
                'classroom' : classroom,
                'marks' : marks,
                }


    return render(request, 'app/home.html', context)


@login_required(login_url='login')
def subject_panel(request, pk):
    classroom = Student.objects.get(id=1).classroom
    subject = Subject.objects.get(id=pk)
    posts = Post.objects.filter(classroom=classroom).filter(subject=subject)
    homeworks = Homework.objects.filter(subject=subject)

    context = {'posts' : posts,
                'subject' : subject,
                'classroom' : classroom,
                'homeworks' : homeworks,
                }


    return render(request, 'app/subject_panel.html', context)


@login_required(login_url='login')
def dashboard(request):
    classroom = Student.objects.get(id=1).classroom
    context = {
        'classroom' : classroom,
    }
    
    
    return render(request, 'app/choice_classroom.html', context)


@login_required(login_url='login')
def classroom_panel(request, pk):
    classroom = Classroom.objects.get(id=pk)
    students = Student.objects.filter(classroom=classroom)

    context = {
        'classroom' : classroom,
        'students' : students,
    }

    return render(request, 'app/dashboard.html', context)
    
