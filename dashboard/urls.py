from django.urls import path
from . import views


urlpatterns = [
    path('', views.choice_classroom, name="choice_classroom"),
    path('classroom/<str:classroom_pk>', views.choice_subject, name="choice_subject"),
    path('classroom/<str:classroom_pk>/subject/<str:subject_pk>', views.dashboard, name="dashboard"),
    path('classroom/<str:classroom_pk>/subject/<str:subject_pk>/posts', views.dashboard_posts, name="dashboard_posts"),
    path('classroom/<str:classroom_pk>/subject/<str:subject_pk>/homeworks', views.dashboard_homeworks, name="dashboard_homeworks"),
    path('classroom/<str:classroom_pk>/subject/<str:subject_pk>/marks', views.dashboard_marks, name="dashboard_marks"),
    path('classroom/<str:classroom_pk>/subject/<str:subject_pk>/lesson_plan', views.dashboard_lesson_plan, name="dashboard_lesson_plan"),

]
