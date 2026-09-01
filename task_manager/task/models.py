from django.db import models
from task_manager.user.models import User
from task_manager.status.models import Status

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    author = models.ForeignKey(User, related_name='created_tasks', on_delete=models.PROTECT)
    performer = models.ForeignKey(User, related_name='assigned_tasks', null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=200)
    # label = models.ManyToManyField(Label, ...)
