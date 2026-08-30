from django import forms
from django.db import models
from task_manager.task.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'status', 'performer']