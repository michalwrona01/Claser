from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user, redirect_to_home_page_due_to_role, redirect_to_choice_profile
from dashboard.forms import PostCreationForm
from django.contrib import messages


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
        'student': student,
        'subjects': subjects,
        'classroom': classroom,
        'marks': marks,
    }

    return render(request, 'app/home.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['student'])
def subject_panel(request, subject_pk):
    classroom = request.user.student.classroom
    subject = classroom.subjects.filter(id=subject_pk).first()
    posts = Post.objects.filter(classroom=classroom).filter(subject=subject)
    homeworks = Homework.objects.filter(subject=subject)

    initial_values = {
        'classroom': classroom,
        'subject': subject,
        'created_person': request.user}

    form_post = PostCreationForm(initial=initial_values)

    if request.method == "POST":

        form_post = PostCreationForm(request.POST, initial=initial_values)
        if form_post.is_valid():
            form_post.save()

    context = {'posts': posts,
               'subject': subject,
               'classroom': classroom,
               'homeworks': homeworks,
               'form_post': form_post,
               }

    return render(request, 'app/subject_panel.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['student'])
def subject_panel_post_delete(request, subject_pk, post_id):
    try:
        post_obj = Post.objects.get(id=post_id)
        if post_obj.created_person == request.user:
            post_obj.delete()
            messages.success(request, "You just delete post!")
        else:
            messages.error(request, "You can't delete this post!")
    except ObjectDoesNotExist:
        messages.error(request, "You doesn't have any posts or want to delete an existing post!")
    finally:
        return redirect('subject_panel', subject_pk)
