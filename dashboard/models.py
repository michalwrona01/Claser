from django.db import models
from django.db.models.fields.related import ForeignKey
from app.models import Classroom, Subject, Teacher
from django.db.models.signals import post_save
from django.dispatch import receiver



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

    #date = models.DateField(null=True)
    day_of_the_week = models.TextField(null=False, max_length=20, choices=DAYS_OF_THE_WEEK)
    lesson_plan = models.ForeignKey(LessonPlan, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lesson_plan.classroom} - {self.day_of_the_week.upper()}'


class Lesson(models.Model):
    number_lesson = models.IntegerField(null=False)
    room  = models.CharField(max_length=10, null=False, default='-')
    hour_start = models.TimeField(auto_now=False, auto_now_add=False, default='00:00:00')
    hour_finish = models.TimeField(auto_now=False, auto_now_add=False, default='00:00:00')

    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE, default=None)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE, default=None)
    day = ForeignKey(Day, null=True, on_delete=models.CASCADE)
    lesson_plan = models.ForeignKey(LessonPlan, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number_lesson}'

    @property
    def get_hour_start_finish(self):
        return f'{self.hour_start} - {self.hour_finish}'


@receiver(post_save, sender=LessonPlan)
def create_days_and_lessons(sender, instance, created, **kwargs):
    if created: 
        for day in Day.DAYS_OF_THE_WEEK:
            day_created = Day.objects.create(lesson_plan=instance, day_of_the_week=day[0])
            for i in range(1, 9):
                Lesson.objects.create(number_lesson=i, day=day_created, lesson_plan=instance)
