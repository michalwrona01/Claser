from django.shortcuts import redirect, render
from django.http import HttpResponse



def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                group = request.user.groups.first().name

            if request.user.groups.first() is None:
                return render(request, 'authentication/choice_user_profile.html', {})

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)

            else:
                return redirect('home')

        return wrapper_func
    return decorator


def redirect_to_home_page_due_to_role(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.first().name == 'student':
            return view_func(request, *args, **kwargs)

        elif request.user.groups.first().name == 'teacher':
            return redirect('choice_classroom')

        elif request.user.groups.first().name == 'director':
            return redirect('choice_classroom')
    return wrapper


def redirect_to_choice_profile(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            request.user.groups.first().name
        except Exception:
            return render(request, 'authentication/choice_user_profile.html', {})
        else:
            return view_func(request, *args, **kwargs)

    return wrapper
