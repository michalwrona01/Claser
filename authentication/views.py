from django.shortcuts import redirect, render
from .forms import UserRegisterForm, StudentCreationForm, TeacherCreationForm, DirectorCreationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .backends import EmailBackend, is_user_has_profile
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def create_profile_director(request):
    form = DirectorCreationForm(initial={'user': request.user})
        
    if request.method == "POST":
        form = DirectorCreationForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
                
            return redirect('home')


    context = {'form' : form}
    return render(request, 'authentication/creation_profile_director.html', context)


@login_required(login_url='login')
def create_profile_teacher(request):
    form = TeacherCreationForm(initial={'user': request.user})
        
    if request.method == "POST":
        form = TeacherCreationForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
                
            return redirect('home')


    context = {'form' : form}
    return render(request, 'authentication/creation_profile_teacher.html', context)


@login_required(login_url='login')
def create_profile_student(request):
    form = StudentCreationForm(initial={'user': request.user})
        
    if request.method == "POST":
        form = StudentCreationForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            form.save()
                
            return redirect('home')


    context = {'form' : form}
    return render(request, 'authentication/creation_profile_student.html', context)


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = EmailBackend().authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)

            if is_user_has_profile(user):
                return redirect('home')
            else:
                return render(request, 'authentication/choice_user_profile.html', {})
        else:
            messages.error(request, 'You entered the wrong e-mail or password.')
            

    return render(request, 'authentication/login.html', {})



def register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, 'Account was created for ' + first_name, last_name)

            return redirect('login')

    context = {'form' : form}

    return render(request, 'authentication/register.html', context)


@login_required(login_url='login')
def logout(request):
    auth_logout(request)

    return redirect('login')

