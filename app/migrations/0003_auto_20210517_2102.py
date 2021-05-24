# Generated by Django 3.2.2 on 2021-05-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_mark_mark_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='classroom',
            new_name='classrooms',
        ),
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='personal_identity_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
