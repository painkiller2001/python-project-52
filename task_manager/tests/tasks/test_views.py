from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user


def test_tasks_view_anonymous(client):
    check_access_anonymous(client, '/tasks/')


def test_tasks_view_logined_user(client, db):
    check_access_logined_user(client, '/tasks/', 'task/tasks.html')