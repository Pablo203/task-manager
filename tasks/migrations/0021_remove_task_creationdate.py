# Generated by Django 4.1.2 on 2022-11-16 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_task_creationdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='creationDate',
        ),
    ]