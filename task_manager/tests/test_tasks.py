from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user


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

    response = check_access_logined_user(client, user_creation, '/tasks/', 'task/tasks.html')
    assert 'tasks' in response.context