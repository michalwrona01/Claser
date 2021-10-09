from dashboard.models import *
from django.shortcuts import redirect, render
from app.models import *
from app.decorators import allowed_user
from django.contrib.auth.decorators import login_required
from .forms import PostCreationForm, HomeworkCreationForm, MarkAddForm
import numpy as np
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def choice_classroom(request):
    classrooms = request.user.teacher.classrooms.all()
    context = {
        'classrooms' : classrooms,
    }
    
    
    return render(request, 'dashboard/choice_classroom.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def choice_subject(request, classroom_pk):
    classroom = Classroom.objects.get(id=classroom_pk)
    teacher_subjects = set(request.user.teacher.subjects.all())
    classroom_subjects = set(classroom.subjects.all())
    subjects = teacher_subjects & classroom_subjects


    context = {
        'classroom' : classroom,
        'subjects' : subjects
    }
    
    
    return render(request, 'dashboard/choice_subject.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def dashboard(request, classroom_pk, subject_pk):
    active_list_for_boostrap = ['', '', '', '', '', '']
    classroom = Classroom.objects.get(id=classroom_pk)
    subject = Subject.objects.get(id=subject_pk)

    context = {
        'active_list' : active_list_for_boostrap,
        'classroom' : classroom,
        'subject' : subject,
    }

    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def dashboard_posts(request, classroom_pk, subject_pk):
    active_list_for_boostrap = ['', 'active', '', '', '', '']
    classroom = Classroom.objects.get(id=classroom_pk)
    subject = Subject.objects.get(id=subject_pk)
    posts = Post.objects.filter(classroom=classroom).filter(subject=subject)

    inital_values_form = {
            'classroom' : classroom,
            'subject' : subject,
            'created_person' : request.user}

    form = PostCreationForm(initial=inital_values_form)

    if request.method == "POST":
        form = PostCreationForm(request.POST, initial=inital_values_form)
        if form.is_valid():
            form.save()

    context = {
        'active_list' : active_list_for_boostrap,
        'classroom' : classroom,
        'subject' : subject,
        'posts' : posts,
        'form' : form
    }

    return render(request, 'dashboard/posts_dashboard.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def dashboard_post_delete(request, classroom_pk, subject_pk, post_pk):
    try:
        post_obj = Post.objects.get(id=post_pk)
    except ObjectDoesNotExist:
        messages.error(request, "You doesn't have any posts or or want to delete an existing post!")
    else:
        post_obj.delete()
        messages.success(request, "You just delete post!")
    finally:
        return redirect('dashboard_posts', classroom_pk, subject_pk)


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def dashboard_homeworks(request, classroom_pk, subject_pk):
    active_list_for_boostrap = ['', '', 'active', '', '', '']
    classroom = Classroom.objects.get(id=classroom_pk)
    subject = Subject.objects.get(id=subject_pk)
    homeworks = Homework.objects.filter(classroom=classroom).filter(subject=subject)

    inital_values_form = {
            'classroom' : classroom,
            'subject' : subject,
            'created_person' : request.user}

    form = HomeworkCreationForm(initial=inital_values_form)

    if request.method == "POST":
        form = HomeworkCreationForm(request.POST, initial=inital_values_form)
        if form.is_valid():
            form.save()

    context = {
        'active_list' : active_list_for_boostrap,
        'classroom' : classroom,
        'subject' : subject,
        'homeworks' : homeworks,
        'form' : form
    }

    return render(request, 'dashboard/homeworks_dashboard.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def dashboard_homework_delete(request, classroom_pk, subject_pk, homework_pk):
    try:
        homework_obj = Homework.objects.get(id=homework_pk)
    except ObjectDoesNotExist:
        messages.error(request, "You doesn't have any homeworks or or want to delete an existing post!")
    else:
        homework_obj.delete()
        messages.success(request, "You just delete homework!")
    finally:
        return redirect('dashboard_homeworks', classroom_pk, subject_pk)


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def dashboard_marks(request, classroom_pk, subject_pk):
    active_list_for_boostrap = ['', '', '', 'active', '', '']
    classroom = Classroom.objects.get(id=classroom_pk)
    subject = Subject.objects.get(id=subject_pk)
    students = Student.objects.filter(classroom=classroom)

    students_and_marks = []
    for student in students:
        marks = Mark.objects.filter(subject_id=subject_pk).filter(students__id=student.id).all()
        students_and_marks.append({student : marks})

    inital_values_form = {
            'classroom' : classroom,
            'subject' : subject,
            'created_person' : request.user
            }
       
    form = MarkAddForm(classroom_pk, inital_values_form) 

    if request.method == "POST":
        form = MarkAddForm(classroom_pk, request.POST, inital_values_form)
        if form.is_valid():
            form.save()


    context = {
        'active_list' : active_list_for_boostrap,
        'classroom' : classroom,
        'subject' : subject,
        'students' : students,
        'students_and_marks' : students_and_marks,
        'forms' : form,
    }
                

    return render(request, 'dashboard/marks_dashboard.html', context)
