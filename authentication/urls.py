from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('choice_profile', views.choice_user_profile, name="choice_user_profile"),
    path('logout', views.logout, name="logout"),
]
