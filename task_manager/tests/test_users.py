from task_manager.tests.helpers import check_access_logined_user, check_access_anonymous


def test_users_view_anonymous(client, db):
    response = client.get('/users/')
    
    assert response.status_code == 200
    assert 'user/users.html' in [t.name for t in response.templates] 


def test_users_view_logined_user(client, user_creation):
    check_access_logined_user(client, user_creation, '/users/', 'user/users.html')


def test_users_update_view_anonymous(client, user_creation):

    user = user_creation
    check_access_anonymous(client, f'/users/{user.id}/update/')


def test_users_delete_view_anonymous(client, user_creation):

    user = user_creation
    check_access_anonymous(client, f'/users/{user.id}/delete/')


def test_statuses_main_view_logined_user(client, user_creation):
    response = check_access_logined_user(client, user_creation, '/statuses/', 'status/statuses.html')
    assert 'statuses' in response.context


def test_statuses_create_view_logined_user(client, user_creation):
    response = check_access_logined_user(client, user_creation, '/statuses/create/', 'status/status_create.html')
    assert 'form' in response.context