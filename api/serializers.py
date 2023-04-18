from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):

    title = serializers.CharField(
        max_length=10,
        required=True,
     
        )
 

    
    class Meta:
        model = Task
        fields = '__all__'

    # def to_representation(self, instance):
    #     return {
    #         "id": instance.id,
    #         "title": instance.title,
    #     }

class UserSerializer(serializers.ModelSerializer):
    
    # tasks_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='tasks')
   


    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'tasks_link']