from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user, redirect_to_home_page_due_to_role, redirect_to_choice_profile
from .forms import PostCreationForm, HomeworkCreationForm



@login_required(login_url='login')
@redirect_to_choice_profile
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

    initial_values = initial={
            'classroom' : classroom,
            'subject' : subject,
            'created_person' : request.user}
    
    form_post = PostCreationForm(initial=initial_values)

    if request.method == "POST":
        form_post = PostCreationForm(request.POST, initial=initial_values)
        if form_post.is_valid():
            form_post.save()


    context = {'posts' : posts,
                'subject' : subject,
                'classroom' : classroom,
                'homeworks' : homeworks,
                'form_post' : form_post,
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

    form = PostCreationForm(initial={
            'classroom' : classroom,
            'subject' : subject,
            'created_person' : request.user})

    if request.method == "POST":
        form = PostCreationForm(request.POST, initial={
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


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def dashboard_homeworks (request, classroom_pk, subject_pk):
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

    return render(request, 'app/homeworks_dashboard.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['teacher'])
def dashboard_marks(request, classroom_pk, subject_pk):
    active_list_for_boostrap = ['', '', '', 'active', '', '']
    classroom = Classroom.objects.get(id=classroom_pk)
    subject = Subject.objects.get(id=subject_pk)
    students = Student.objects.filter(classroom=classroom)

    students_and_marks = []
    
    for student in students:
        marks = Mark.objects.filter(students__id=student.id).all()
        students_and_marks.append({student : marks})


    context = {
        'active_list' : active_list_for_boostrap,
        'classroom' : classroom,
        'subject' : subject,
        'students' : students,
        'students_and_marks' : students_and_marks,
    }
                

    return render(request, 'app/marks_dashboard.html', context)

    



    
