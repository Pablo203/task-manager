from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=100)
    longDescription = models.CharField(max_length=500)

    category = models.CharField(max_length=50)

    stateOptions = models.TextChoices('state', 'toDo inProgress done')
    state = models.CharField(blank=True, max_length=10, choices=stateOptions.choices)
    priority = models.IntegerField()

    def __str__(self):
        return self.name