from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
# add this for authentication
from rest_framework.permissions import IsAuthenticated 
from .models import Task
from .serializers import TaskSerializer, UserSerializer
# Import the user model
from django.contrib.auth.models import User

class TaskView(APIView):
 
    permission_classes = [IsAuthenticated] # 
    def get(self, request: Request) -> Response:
        '''get all tasks'''
        user = request.user
        tasks = Task.objects.filter(student=user)
        serializer = TaskSerializer(tasks, many=True)
        data = serializer.data
        return Response(data)
    
    def post(self, request: Request) -> Response:
        '''add task'''
        data = request.data
        user = request.user 
        task = Task.objects.create(
            title=data['title'],
            description=data['description'],
            student=user,
        )
        task.save()
        return Response(data)
        
    
    def put(self, request: Request, pk: int) -> Response:
        '''uodate task'''
        try:
            task = Task.objects.get(id=pk)
        except ObjectDoesNotExist:
            return Response({'error': 'does not exist'})
        
        data = request.data
        serializer = TaskSerializer(task, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
# Get all users
class UserView(APIView):
    def get(self, request: Request,user:str) -> Response:
        '''Get all user's tasks'''
        user = User.objects.get(username=user)
        serializer = UserSerializer(user)
        data = serializer.data
        return Response(data)
  