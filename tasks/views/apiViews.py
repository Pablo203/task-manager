from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Task
from ..serializers import TaskSerializer

@api_view(['GET', 'POST'])
def getAll(request, format=None):
    if request.method == 'GET':
        tasks = Task.objects.filter(createdBy=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)