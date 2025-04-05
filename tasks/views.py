from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
from .serializers import TaskSerializer

# -------------------------
# ✅ Custom Task Form
# -------------------------
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed']

# -------------------------
# ✅ Homepage
# -------------------------
def home(request):
    return HttpResponse("<h1>Welcome to Task Manager API</h1><p>Visit /swagger/ for API docs.</p>")

# -------------------------
# ✅ DRF API View
# -------------------------
class TaskListView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# -------------------------
# ✅ Authentication Views
# -------------------------
class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'

class RegisterView(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')
        return super().get(request, *args, **kwargs)

def logout_view(request):
    logout(request)
    return redirect('login')

# -------------------------
# ✅ Task Views
# -------------------------
@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
@csrf_exempt
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('dashboard')

# -------------------------
# ✅ Class-Based CRUD Views
# -------------------------
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
