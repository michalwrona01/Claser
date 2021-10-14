from django.db import models

from app.models import Classroom, Subject, Teacher

class Lesson(models.Model):
    date = models.DateField()
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    time = models.TimeField()
