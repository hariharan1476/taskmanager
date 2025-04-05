# tasks/api_urls.py

from django.urls import path
from . import api_views  # You must create this file

urlpatterns = [
    path('', api_views.TaskListAPI.as_view(), name='api-task-list'),
    path('<int:pk>/', api_views.TaskDetailAPI.as_view(), name='api-task-detail'),
]
