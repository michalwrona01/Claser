from django.db import models
from django.db.models.fields.related import ForeignKey
from app.models import Classroom, Subject, Teacher



class LessonPlan(models.Model):
    classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.classroom}'


class Day(models.Model):
    DAYS_OF_THE_WEEK = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
    )

    date = models.DateField()
    day_of_the_week = models.TextField(null=False, max_length=20, choices=DAYS_OF_THE_WEEK)
    lessonplan = models.ForeignKey(LessonPlan, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lessonplan.classroom} - {self.day_of_the_week}'


class Lesson(models.Model):
    number_lesson = models.IntegerField(null=False)
    room  = models.CharField(max_length=10, null=False)
    hour_start = models.TimeField(auto_now=False, auto_now_add=False)
    hour_finish = models.TimeField(auto_now=False, auto_now_add=False)

    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    day = ForeignKey(Day, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject}'



