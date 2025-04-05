from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    TaskList, TaskDetail, TaskCreateView, TaskUpdateView, TaskDeleteView,
    CustomLoginView, RegisterView, complete_task, dashboard, home
)

urlpatterns = [
    # Home and Dashboard
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),

    # Task CRUD UI
    path('tasks/', TaskList.as_view(), name='task-list'),                # List all tasks
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),   # View task detail
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'), # Create new task
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),  # Update task
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),  # Delete task
    path('tasks/complete/<int:task_id>/', complete_task, name='task-complete'),    # Complete task

    # Auth
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
