from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('subject_panel/<str:pk>', views.subject_panel, name="subject_panel"),
]
