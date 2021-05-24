from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user, redirect_to_home_page_due_to_role
from .forms import PostAddForm



@login_required(login_url='login')
@redirect_to_home_page_due_to_role
@allowed_user(allowed_roles=['student'])
def home(request):
    student = Student.objects.get(user=request.user)
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
@allowed_user(allowed_roles=['student'])
def subject_panel(request, pk):
    classroom = request.user.student.classroom
    subject = classroom.subjects.filter(id=pk).first()
    posts = Post.objects.filter(classroom=classroom).filter(subject=subject)
    homeworks = Homework.objects.filter(subject=subject)


    context = {'posts' : posts,
                'subject' : subject,
                'classroom' : classroom,
                'homeworks' : homeworks,
                }


    return render(request, 'app/subject_panel.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def choice_classroom(request):
    classrooms = request.user.teacher.classrooms.all()
    context = {
        'classrooms' : classrooms,
    }
    
    
    return render(request, 'app/choice_classroom.html', context)

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
    
    
    return render(request, 'app/choice_subject.html', context)


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

    return render(request, 'app/dashboard.html', context)

@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def dashboard_posts(request, classroom_pk, subject_pk):
    active_list_for_boostrap = ['', 'active', '', '', '', '']
    classroom = Classroom.objects.get(id=classroom_pk)
    subject = Subject.objects.get(id=subject_pk)
    posts = Post.objects.filter(classroom=classroom).filter(subject=subject)

    form = PostAddForm(initial={
            'classroom' : classroom,
            'subject' : subject,
            'created_person' : request.user})

    if request.method == "POST":
        form = PostAddForm(request.POST, initial={
            'classroom' : classroom,
            'subject' : subject,
            'created_person' : request.user})
        if form.is_valid():
            form.save()

    context = {
        'active_list' : active_list_for_boostrap,
        'classroom' : classroom,
        'subject' : subject,
        'posts' : posts,
        'form' : form
    }

    return render(request, 'app/posts_dashboard.html', context)
    
