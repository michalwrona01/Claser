from django.db import models


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

class Person(models.Model):
    name = models.CharField(max_length=20, null=False)
    classroom = models.ForeignKey(Classroom, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.classroom.name}'

class Mark(models.Model):
    MARK_NUMBER = (
        (1, '1'),
        (1.5 , '1+'),
        (2, '2'),
        (2.5, '2+'),
        (3, '3'),
        (3.5, '3+'),
        (4, '4'),
        (4.5, '4+'),
        (5, '5'),
        (5.5, '5+'),
        (6, '6'),
    )
    mark_number = models.IntegerField(null=False, choices=MARK_NUMBER)
    subjects = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    students = models.ManyToManyField(Person)

    def __str__(self):
        return str(self.mark_number)

class Post(models.Model):
    text = models.CharField(max_length=1000, null=False)
    date_created = models.DateField(auto_now_add=True)
    classroom = models.ForeignKey(Classroom, null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    created_person = models.ForeignKey(Person, null=True, on_delete=models.CASCADE)


class Homework(models.Model):
    text = models.CharField(max_length=500, null=False)
    subject = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Message(models.Model):
    text = models.CharField(max_length=1000, null=False)

    