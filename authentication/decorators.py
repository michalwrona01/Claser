from django.http import HttpResponse, request
from django.shortcuts import redirect


def unauthenticated_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def without_profile_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.exists():
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
            
    return wrapper
