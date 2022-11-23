from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from ..models import Task
from ..serializers import TaskSerializer, TaskStateSerializer

@api_view(['GET', 'POST'])
def getAll(request, format=None):
    if request.method == 'GET':
        tasks = Task.objects.filter(createdBy=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def changeState(request, taskId, state, format=None):
    task = Task.objects.get(id=taskId)
    if request.method == 'PUT':
        serializer = TaskStateSerializer(task, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)