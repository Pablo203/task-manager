# Generated by Django 4.1.2 on 2022-11-16 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_rename_projectname_task_projectid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='filePath',
        ),
    ]