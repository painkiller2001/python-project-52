from django import forms
from django.db import models
from task_manager.status.models import Status
from django.contrib.auth.forms import UserCreationForm

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']