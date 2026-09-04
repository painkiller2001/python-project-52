from django import forms
from django.db import models
from task_manager.task.models import Task
from task_manager.status.models import Status
from task_manager.user.models import User
from task_manager.label.models import Label



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'status', 'performer', 'description', 'label']


class TaskFilterForm(forms.Form):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=False,
        empty_label='Не выбрано',
        label='Статус'
    )
    performer = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        empty_label='Не выбрано',
        label='Исполнитель'
    )
    label = forms.ModelChoiceField(
        queryset=Label.objects.all(),
        required=False,
        empty_label='Не выбрано',
        label='Метка'
    )