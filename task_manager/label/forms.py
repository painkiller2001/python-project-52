from django import forms
from django.db import models
from task_manager.label.models import Label
from django.contrib.auth.forms import UserCreationForm

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']