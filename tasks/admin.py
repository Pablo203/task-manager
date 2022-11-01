from django.contrib import admin
from .models import Task, Project, File

# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(File)