# tasks/api_views.py

from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListAPI(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
