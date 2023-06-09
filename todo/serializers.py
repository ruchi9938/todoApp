from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    """Serializer for retrieving and updating ToDo items."""

    class Meta:
        model = TodoItem
        fields = ('id', 'title', 'completed')

class TodoItemCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating ToDo items."""

    class Meta:
        model = TodoItem
        fields = ('title', 'completed')
