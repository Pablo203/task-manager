# Generated by Django 4.1.2 on 2022-11-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_remove_task_filepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='projectId',
            field=models.IntegerField(),
        ),
    ]