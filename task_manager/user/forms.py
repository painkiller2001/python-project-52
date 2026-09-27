from django.contrib.auth.forms import UserCreationForm

from task_manager.user.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
