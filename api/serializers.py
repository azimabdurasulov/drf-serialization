from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    # def to_representation(self, instance):
    #     return {
    #         "id": instance.id,
    #         "title": instance.title,
    #     }
