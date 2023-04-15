from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    class Meta:
        model = Task
        fields = '__all__'

    # def to_representation(self, instance):
    #     return {
    #         "id": instance.id,
    #         "title": instance.title,
    #     }

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='completed'
    )

    class Meta:
        model = User
        fields = ('username', 'tasks')