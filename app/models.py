from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=25, null=False)
    date_created = models.DateField(auto_now_add=True)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name

class Student(models.Model):
    is_student = models.BooleanField(default=True)
    classroom = models.ForeignKey(Classroom, null=True, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True)
    personal_identity_number = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.classroom}'


class Mark(models.Model):
    MARK_NUMBER = (
        (1, '1'),
        (1.5 , '1+'),
        (1.75, '-2'),
        (2, '2'),
        (2.5, '2+'),
        (2.75, '-3'),
        (3, '3'),
        (3.5, '3+'),
        (3.75, '-4'),
        (4, '4'),
        (4.5, '4+'),
        (4.75, '-5'),
        (5, '5'),
        (5.5, '5+'),
        (5.75, '-6'),
        (6, '6'),
    )
    mark_number = models.FloatField(null=False, choices=MARK_NUMBER)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return str(self.mark_number)

class Post(models.Model):
    text = models.CharField(max_length=1000, null=False)
    date_created = models.DateField(auto_now_add=True)
    classroom = models.ForeignKey(Classroom, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    created_person = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Homework(models.Model):
    task = models.CharField(max_length=500, null=False)
    text = models.CharField(max_length=500, null=True)
    subject = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, null=False, on_delete=models.CASCADE)
    deadline_date = models.DateField(null=False)

class Message(models.Model):
    text = models.CharField(max_length=1000, null=False)


class Teacher(models.Model):
    is_teacher = models.BooleanField(default=True)
    classroom = models.ManyToManyField(Classroom)
    subjects = models.ManyToManyField(Subject)

    user = models.OneToOneField(User, on_delete=models.CASCADE)