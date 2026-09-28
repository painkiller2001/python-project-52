import pytest

from task_manager.label.models import Label
from task_manager.status.models import Status
from task_manager.user.models import User
from task_manager.task.models import Task


@pytest.fixture
def user_creation(db):
    user = User.objects.create_user(username='test_uesr', password='12345qqQ!')
    return user


@pytest.fixture
def task_creation(db, user_creation, status_creation):
    task = Task.objects.create(name='test_task', author=user_creation, status=status_creation)
    return task


@pytest.fixture
def label_creation(db):
    label = Label.objects.create(name='test_label')
    return label


@pytest.fixture
def status_creation(db):
    status = Status.objects.create(name='test_status')
    return status