from task_manager.tests.helpers import check_access_logined_user, check_access_anonymous


def test_users_main_view_anonymous(client, db):
    response = client.get('/users/')
    assert response.status_code == 200
    assert 'user/users.html' in [t.name for t in response.templates] 


# def test_users_create_view_anonymous(client, user_creation):
#     response = check_access_logined_user(client, user_creation, '/users/create/', 'user/user_create.html')
#     assert 'form' in response.context 


def test_users_update_view_anonymous(client):
    check_access_anonymous(client, f'/users/{user.id}/update/')


def test_users_delete_view_anonymous(client):
    check_access_anonymous(client, f'/users/{user.id}/delete/')


def test_users_main_view_logined_user(client, user_creation):
    user = user_creation
    response = check_access_logined_user(client, user_creation, '/users/', 'user/users.html')
    assert 'users' in response.context


def test_users_create_view_logined_user(client, user_creation):
    response = check_access_logined_user(client, user_creation, '/users/create/', 'user/user_create.html')
    assert 'form' in response.context






