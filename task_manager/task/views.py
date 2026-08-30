from django.shortcuts import render
from django.views import View
from task_manager.task.models import Task

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
        ...

    def post(self, request, *args, **kwargs):
        ...
    

class TaskUpdateView(View):

    def get(self, request, *args, **kwargs):
        ...

    def post(self, request, *args, **kwargs):
        ...
    

class TaskDeleteView(View):

    def get(self, request, *args, **kwargs):
        ...

    def post(self, request, *args, **kwargs):
        ...