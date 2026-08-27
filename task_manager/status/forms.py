from django import forms
from task_manager.user.models import User
from django.contrib.auth.forms import UserCreationForm

class StatusForm(forms.Form):
    ...