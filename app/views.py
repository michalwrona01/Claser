from django.shortcuts import render
from django.http import HttpResponse
from .models import *


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


    return render(request, 'app/dashboard.html', context)