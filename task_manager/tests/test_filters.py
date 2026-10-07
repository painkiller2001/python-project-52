from task_manager.task.models import Task
from task_manager.user.models import User
from task_manager.label.models import Label
from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user


# def task_filtered_view_by_status(client, user_creation):

#     client.force_login(user_creation)

#     url = f'/tasks/'

#     task1 = Task.objects.create
#     task2 = 

#     ?status=2&performer=&label=

    
def test_task_filtered_view_by_performer(client, user_creation, label_creation, status_creation, task_creation):
    
    client.force_login(user_creation)

    another_performer = User.objects.create_user(username='Another_Performer', password='12345qqQ!')

    task = Task.objects.create(name='test_task2', author=user_creation, performer=user_creation, status=status_creation)
    task2 = Task.objects.create(name='test_task2', author=user_creation, performer=another_performer, status=status_creation)

    url = f'/tasks/?status=&performer={user_creation.id}&label=&own_tasks='

    response = client.get(url)

    assert response.status_code == 200
    assert task in response.context['tasks']
    assert task2 not in response.context['tasks']


def test_task_filtered_view_by_label(client, user_creation, label_creation, status_creation, task_creation):
    
    client.force_login(user_creation)

    another_label = Label.objects.create(name='Test_label')

    task = task_creation
    task.label.add(label_creation)
    task2 = Task.objects.create(name='test_task2', author=user_creation, performer=user_creation, status=status_creation)
    task2.label.add(another_label)

    url = f'/tasks/?status=&performer=&label={label_creation.id}&own_tasks='

    response = client.get(url)

    assert response.status_code == 200
    assert task in response.context['tasks']
    assert task2 not in response.context['tasks']


def test_task_filtered_view_own_tasks(client, user_creation, status_creation, task_creation):
    
    client.force_login(user_creation)

    another_user = User.objects.create_user(username='Another_User', password='12345qqQ!')

    task = task_creation
    task2 = Task.objects.create(name='test_task2', author=another_user, performer=user_creation, status=status_creation)

    url = f'/tasks/?status=&performer=&label=&own_tasks=on'

    response = client.get(url)

    assert response.status_code == 200
    assert task in response.context['tasks']
    assert task2 not in response.context['tasks'] 

