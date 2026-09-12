from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user


def test_tasks_view_anonymous(client, db):
    response = client.get('/users/')
    
    assert response.status_code == 200
    assert 'user/users.html' in [t.name for t in response.templates] 


def test_users_view_logined_user(client, db):
    check_access_logined_user(client, '/users/', 'user/users.html')