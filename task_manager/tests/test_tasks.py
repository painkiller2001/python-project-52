from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user


def test_tasks_view_anonymous(client):
    check_access_anonymous(client, '/tasks/')


def test_tasks_view_logined_user(client, user_creation):
    check_access_logined_user(client, user_creation, '/tasks/', 'task/tasks.html')


