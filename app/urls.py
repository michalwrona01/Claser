from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('subject_panel/<str:subject_pk>', views.subject_panel, name="subject_panel"),
    path('subject_panel/<str:subject_pk>/posts/<str:post_id>/delete', views.subject_panel_post_delete, name="subject_panel_post_delete"),
]
