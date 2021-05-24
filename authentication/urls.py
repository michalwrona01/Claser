from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('create_profile/student', views.create_profile_student, name="create_profile_student"),
    path('create_profile/teacher', views.create_profile_teacher, name="create_profile_teacher"),
    path('create_profile/director', views.create_profile_director, name="create_profile_director"),
    path('logout', views.logout, name="logout"),
]
