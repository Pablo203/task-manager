# Generated by Django 4.1.2 on 2022-11-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_filepath'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='projectName',
            field=models.CharField(default='', max_length=100),
        ),
    ]