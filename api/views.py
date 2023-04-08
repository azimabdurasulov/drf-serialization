from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(APIView):
    def get(self, request: Request) -> Response:
        '''get all tasks'''
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        data = serializer.data
        return Response(data)
    
    def post(self, request: Request) -> Response:
        '''add task'''
        data = request.data
        serialzer = TaskSerializer(data=data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        
        return Response(serialzer.errors)
    