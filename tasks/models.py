from django.db import models
from django.conf import settings

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, default='')
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, default='')

    category = models.CharField(max_length=50)

    stateOptions = models.TextChoices('state', 'toDo inProgress done')
    state = models.CharField(blank=True, max_length=10, choices=stateOptions.choices)
    priority = models.IntegerField()

    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    projectName = models.ForeignKey(Project, on_delete=models.CASCADE, default='')
    projectId = models.IntegerField(editable=False)
    
    def __str__(self):
        return self.name