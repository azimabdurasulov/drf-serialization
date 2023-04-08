from rest_framework import serializers

class Task():
    def __init__(self, id, title, description, done):
        self.id          = id
        self.title       = title
        self.description = description
        self.done        = done


class TaskSerializer(serializers.Serializer):
    id          = serializers.IntegerField()
    title       = serializers.CharField()
    description = serializers.CharField()
    done        = serializers.BooleanField()

    def create(self, validated_data):
        return Task(**validated_data)


data = {
    'id': 1,
    'title': 'title',
    'description': 'description',
    'done': False
}
serializer = TaskSerializer(data=data)
if serializer.is_valid():
    task = serializer.save()
    print(task.title)