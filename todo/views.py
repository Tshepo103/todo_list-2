from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone
from django.contrib import messages


def index(request):
    tasks = Task.objects.all().order_by('due_date')
    for task in tasks:
        task.remaining_time = task.time_left()
    return render(request, 'todo/index.html', {
        'tasks': tasks,
        'now': timezone.now(),
        
     })

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'todo/form.html', {'form': form, 'title': 'Add Task'})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated!')
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/form.html', {'form': form, 'title': 'Edit Task'})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    messages.success(request, 'Task deleted.')
    return redirect('index')

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    messages.success(request, 'Task marked as complete.')
    return redirect('index')

def login_view(request):
    # Placeholder for login view logic
    return render(request, 'todo/login.html', {})