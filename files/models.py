from django.db import models
from tasks.models import Task
from django.conf import settings

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=100, default='')
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    originTask = models.ForeignKey(Task, on_delete=models.CASCADE)
    localisation = models.CharField(max_length=200, default='')

    # stateOptions = models.TextChoices('state', 'awaits_approval approved priced accepted')
    # state = models.CharField(blank=True, max_length=10, choices=stateOptions.choices)

    def __str__(self):
        return self.name