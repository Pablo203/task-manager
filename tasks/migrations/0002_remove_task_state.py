# Generated by Django 4.1.2 on 2022-10-13 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='state',
        ),
    ]
