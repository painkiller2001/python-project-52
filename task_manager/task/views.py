from django.shortcuts import render
from django.views import View

# Create your views here.
class TasksView(View):

    def get(self, request, *args, **kwargs):
        ...


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