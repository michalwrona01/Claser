# Generated by Django 3.2.2 on 2021-05-31 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_mark_created_person'),
        ('dashboard', '0003_lesson_classroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.classroom'),
        ),
    ]
