## Table of contents
* [Description](#description)
* [Technologies](#technologies)
* [Setup](#setup)
* [Live demo](#application-demo)
* [Ilustrate](#ilustrate)
* [Features](#features)
* [To Do](#to-do)
* [Project Status](#project-status)
* [Inspiration](#inspiration)

# CLASER
## Description
Web application that allows the school to
manage student grades, homework and
lesson plan with video chat. The project solves 
the problem of today's distance learning. 
The aim of the project is to create a friendly and usable design.

# Technologies
* [Python 3.9.4](https://www.python.org/)
* [Django 3.3.2](https://www.djangoproject.com/)
* [PostgreSQL](https://www.postgresql.org/)
* For stylistic correctness I use [Bootstrap v5](https://getbootstrap.com/)

# Setup
## Application demo
[https://claser.wronamichal.pl/](https://claser.wronamichal.pl/)

## On your PC
### Windows
```bash
virtualenv env
```
```bash
source env/Scripts/activate
```
```bash
pip install requirements.txt
```
```bash
python manage.py runserver
```
Enter your browser on this link: [127.0.0.1:8000](http://127.0.0.1:8000/)
### Linux
```bash
python3 -m venv env
```
```bash
source env/bin/activate
```
```bash
pip install requirements.txt
```
```bash
python manage.py runserver
```
Enter your browser on this link: [127.0.0.1:8000](http://127.0.0.1:8000/)

# Ilustrate

## Login page
![Login page](images_readme/login_page.PNG)

## Student panel
![Student panel](images_readme/student_panel.PNG)

## Teacher panel
### Posts
![Student panel](images_readme/teacher_panel_posts.PNG)

### Homeworks
![Student panel](images_readme/teacher_panel_homework.PNG)

### Marks
![Student panel](images_readme/teacher_panel_marks.PNG)

# Features
- Different profiles
  - Student
  - Teacher
  - Director
- Homeworks
  - Add homework 
  - Delete homework
- Marks
  - Add mark
  - Delete mark
- Posts
  - Add post
  - Delete post
- Lesson Plan
- Video chat
- Attendance list
- Messages

## To do
- Lesson Plan
- Video chat
- Messages
- Director panel

# Project status
The project is in progress development, all changes and development can be seen in the project demo.

[DEMO LIVE](https://claser.wronamichal.pl/) (In the process of migrating to new servers)

# Inspiration
The current situation in the world was the inspiration for creating this application.

# Contact to me
E-mail: wronamichal01@gmail.com




