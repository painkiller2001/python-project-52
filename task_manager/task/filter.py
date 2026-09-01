from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from task_manager.task.models import Task
from task_manager.task.forms import TaskForm
from django.contrib import messages

# Create your views here.
class TasksFilterView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        params = {
            'status': request.GET.get('status'),
            'performer': request.GET.get('performer'),
            # 'label': request.GET.get('')
        }
        return render(
            request,
            'task/tasks.html',
            context={
                'tasks': tasks
            }
        )