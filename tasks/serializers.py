from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'category', 'state', 'priority', 'createdBy']

class TaskStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'state']