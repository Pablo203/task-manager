# Generated by Django 4.1.2 on 2022-10-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_createdby'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='filePath',
            field=models.CharField(default='', max_length=20),
        ),
    ]