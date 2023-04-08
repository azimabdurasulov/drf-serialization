from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(APIView):
    def get(self, request: Request) -> Response:
        '''get all tasks'''
        task = Task.objects.first()
        serializer = TaskSerializer(task)
        data = serializer.data
        return Response(data)
    