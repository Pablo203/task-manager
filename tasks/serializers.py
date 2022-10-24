from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'shortDescription', 'longDescription', 'category', 'state', 'priority', 'createdBy']