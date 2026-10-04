from task_manager.task.models import Task
from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user
from task_manager.user.models import User


def test_tasks_main_view_anonymous(client):
    check_access_anonymous(client, '/tasks/')


def test_tasks_create_view_anonymous(client):
    check_access_anonymous(client, '/tasks/create/')


def test_tasks_update_view_anonymous(client, task_creation):

    task = task_creation
    check_access_anonymous(client, f'/tasks/{task.id}/update/')


def test_tasks_delete_view_anonymous(client, task_creation):

    task = task_creation
    check_access_anonymous(client, f'/tasks/{task.id}/delete/')
    

def test_tasks_main_view_logined_user(client, user_creation):

    response = check_access_logined_user(client, user_creation, '/tasks/', 'task/tasks.html')
    assert 'tasks' in response.context


def test_tasks_create_view_logined_user(client, user_creation):

    response = check_access_logined_user(client, user_creation, '/tasks/create/', 'task/task_create.html')
    assert 'form' in response.context


def test_tasks_update_view_logined_user(client, user_creation, task_creation):

    task = task_creation
    response = check_access_logined_user(client, user_creation, f'/tasks/{task.id}/update/', 'task/task_update.html')
    assert response.context['task'] == task


def test_tasks_delete_view_logined_user(client, user_creation, task_creation):

    task = task_creation
    check_access_logined_user(client, user_creation, f'/tasks/{task.id}/delete/', 'task/delete_confirmation.html')


def test_update_own_task(client, user_creation, task_creation):

    client.force_login(user_creation)
    task = task_creation
    
    url = f'/tasks/{task.id}/update/'

    new_query_data = {
        'name': 'Updated_name',
        'author': task.author,
        'performer': task.perfomer,
        'status': task.status
    }

    response = client.get(url, new_query_data)

    assert response.status_code == 302
    assert '/tasks/' in response.url
    assert not Task.objects.filter(id=task.id, name='Updated_name').exists()


# def test_update_another_task(client, user_creation, task_creation, status_creation):

#     client.force_login(user_creation)
#     task = task_creation
#     user2 = User.objects.create_user(username='Another_User', password='12345qqQ!')
#     task2 = Task.objects.create(name='test_task2', author=user2, performer=user_creation, status=status_creation)
    
#     url = f'/tasks/{task2.id}/update/'

#     response = client.get(url, new_query_data)

#     assert response.status_code == 302
#     assert '/tasks/' in response.url
#     assert Task.objects.filter(id=task2.id).exists()


def test_delete_own_task(client, user_creation, task_creation):

    client.force_login(user_creation)
    task = task_creation
    
    url = f'/tasks/{task.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/tasks/' in response.url
    assert not Task.objects.filter(id=task.id).exists()


def test_delete_another_task(client, user_creation, task_creation, status_creation):

    client.force_login(user_creation)
    task = task_creation
    user2 = User.objects.create_user(username='Another_User', password='12345qqQ!')
    task2 = Task.objects.create(name='test_task2', author=user2, performer=user_creation, status=status_creation)
    
    url = f'/tasks/{task2.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/tasks/' in response.url
    assert Task.objects.filter(id=task2.id).exists()


def test_update_own_task(client, user_creation, task_creation):

    client.force_login(user_creation)
    task = task_creation
    
    url = f'/tasks/{task.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/tasks/' in response.url
    assert not Task.objects.filter(id=task.id).exists()


def test_update_another_task(client, user_creation, task_creation, status_creation):

    client.force_login(user_creation)
    task = task_creation
    user2 = User.objects.create_user(username='Another_User', password='12345qqQ!')
    task2 = Task.objects.create(name='test_task2', author=user2, performer=user_creation, status=status_creation)
    
    url = f'/tasks/{task2.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/tasks/' in response.url
    assert Task.objects.filter(id=task2.id).exists()