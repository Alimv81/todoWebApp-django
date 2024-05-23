from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, TaskUpdateForm


@login_required(login_url='accounts:login', redirect_field_name='')
def index(request):
    return render(request, 'Tasks/index.html', {})


def about_page(request):
    return render(request, 'Tasks/about.html', {})


@login_required(login_url='accounts:login', redirect_field_name='')
def task_list(request, show_done=0):
    if request.method == 'POST':
        if show_done:
            list_object = Task.objects.filter(user=request.user)
            return render(request, 'Tasks/task_list.html',
                          {'task_list': list_object, 'show_done': show_done})

    list_object = Task.objects.filter(user=request.user, done=False)
    return render(request, 'Tasks/task_list.html',
                  {'task_list': list_object, 'show_done': show_done})


@login_required(login_url='accounts:login', redirect_field_name='')
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('Tasks:task-list', 0)
    else:
        form = TaskForm()
    return render(request, 'Tasks/task_create.html', {'form': form})


@login_required(login_url='accounts:login', redirect_field_name='')
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('Tasks:task-list', 0)
    else:
        form = TaskUpdateForm(instance=task)
    return render(request, 'Tasks/task_update.html', {'form': form})


@login_required(login_url='accounts:login', redirect_field_name='')
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('Tasks:task-list', 0)
    return render(request, 'Tasks/task_confirm_delete.html', {'task': task})
