from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Task._meta.get_field('user').remote_field.model.objects.all(),
        label="Admin"  # This changes the display name in the DRF UI
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'is_completed', 'user']  # user (Admin) at last
