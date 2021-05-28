from django.contrib import admin
from django.contrib.admin.sites import DefaultAdminSite
from .models import *

admin.site.register(LessonPlan)
admin.site.register(Day)
admin.site.register(Lesson)
