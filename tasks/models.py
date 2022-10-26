from django.db import models
from django.conf import settings

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=100)
    longDescription = models.CharField(max_length=500)

    category = models.CharField(max_length=50)

    stateOptions = models.TextChoices('state', 'toDo inProgress done')
    state = models.CharField(blank=True, max_length=10, choices=stateOptions.choices)
    priority = models.IntegerField()

    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )

    filePath = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name