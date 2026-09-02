from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from task_manager.task.models import Task
from task_manager.task.forms import TaskForm, TaskFilterForm
from django.contrib import messages

# Create your views here.
class TasksView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        form = TaskFilterForm(request.GET)
        params = {
            'status_id': request.GET.get('status'),
            'performer_id': request.GET.get('performer')
            # 'label__id': request.GET.get('label')
        }
        params = {k: v for k, v in params.items() if v}
        filtered_tasks = tasks.filter(**params)
        return render(
            request,
            'task/tasks.html',
            context={
                'tasks': filtered_tasks,
                'form': form
            }
        )


class TaskDetailView(View):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = get_object_or_404(Task, id=task_id)
        return render(
            request,
            'task/task_detail.html',
            context={
                'task': task
            }
        )


class TaskCreateView(View): 

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(
            request,
            'task/task_create.html',
            context={
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            form.save()
            messages.success(request, 'Задача успешно создана')
            return redirect(
                'tasks'
            )
        else:
            messages.warning(request, 'Задача уже существует')
        return render(
            request,
            'task/task_create.html',
            context={
                'form': form
            }
        )          
    

class TaskUpdateView(View):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id') 
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(
            request,
            'task/task_update.html',
            context={
                'task': task,
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('id') 
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задача успешно обновлена')
            return redirect(
                'tasks'
            )
        return render (
            request,
            'task/task_update.html',
            context={
                'task': task,
                'form': form
            }
        )
    

class TaskDeleteView(View):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id') 
        task = Task.objects.get(id=task_id)
        return render (
            request,
            'task/delete_confirmation.html',
            context={
                'task': task
            }
        )

    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('id') 
        task = Task.objects.get(id=task_id)
        if task:
            task.delete()
            messages.success(request, 'Задача успешно удалена')
            return redirect('tasks')
        return render(
            request,
            'task/delete_confirmation.html',
            context={
                'task': task
            }
        )