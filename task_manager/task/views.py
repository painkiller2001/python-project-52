from django.shortcuts import render
from django.views import View
from task_manager.task.models import Task
from task_manager.task.forms import TaskForm

# Create your views here.
class TasksView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(
            request,
            'task/task_create.html',
            context={
                'tasks': tasks
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
        ...
    

class TaskUpdateView(View):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id') 
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render (
            request,
            'task/task_update.html',
            context={
                'task': task,
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        ...
    

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
        ...