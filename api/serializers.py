from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    completed = serializers.BooleanField(default=False)
    description = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.title
        }
