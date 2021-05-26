from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('subject_panel/<str:pk>', views.subject_panel, name="subject_panel"),
    path('dashboard', views.choice_classroom, name="choice_classroom"),
    path('dashboard/classroom/<str:classroom_pk>', views.choice_subject, name="choice_subject"),
    path('dashboard/classroom/<str:classroom_pk>/subject/<str:subject_pk>', views.dashboard, name="dashboard"),
    path('dashboard/classroom/<str:classroom_pk>/subject/<str:subject_pk>/posts', views.dashboard_posts, name="dashboard_posts"),
    path('dashboard/classroom/<str:classroom_pk>/subject/<str:subject_pk>/homeworks', views.dashboard_homeworks, name="dashboard_homeworks"),
    path('dashboard/classroom/<str:classroom_pk>/subject/<str:subject_pk>/marks', views.dashboard_marks, name="dashboard_marks"),
]
