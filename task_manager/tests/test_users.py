from task_manager.task.models import Task
from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user
from task_manager.user.models import User


def test_user_main_view_anonymous(client, db):
    response = client.get('/users/')
    assert response.status_code == 200
    assert 'user/users.html' in [t.name for t in response.templates] 


def test_user_create_view_anonymous(client, user_creation):
    response = check_access_logined_user(client, user_creation, '/users/create/', 'user/user_create.html')
    assert 'form' in response.context 


def test_user_update_view_anonymous(client, user_creation):
    user = user_creation
    check_access_anonymous(client, f'/users/{user.id}/update/')


def test_user_delete_view_anonymous(client, user_creation):
    user = user_creation
    check_access_anonymous(client, f'/users/{user.id}/delete/')


def test_user_main_view_logined_user(client, user_creation):
    user = user_creation
    response = check_access_logined_user(client, user_creation, '/users/', 'user/users.html')
    assert 'users' in response.context


def test_user_create_view_logined_user(client, user_creation):
    response = check_access_logined_user(client, user_creation, '/users/create/', 'user/user_create.html')
    assert 'form' in response.context


def test_user_update_own_profile(client, user_creation):

    client.force_login(user_creation)
    user = user_creation
    url = f'/users/{user.id}/update/'

    response = client.get(url)

    current_user = response.wsgi_request.user
    logged_in_user_id = current_user.id

    response = check_access_logined_user(client, user_creation, f'/users/{user.id}/update/', 'user/user_update.html')
    assert response.context['user'] == user


def test_user_update_another_profile(client, user_creation):

    client.force_login(user_creation)
    user1 = user_creation
    user2 = User.objects.create(username='Another_User', password='12345qqQ!')
    url = f'/users/{user2.id}/update/'

    response = client.get(url)

    assert response.status_code == 302
    assert '/users/' in response.url



def test_user_delete_own_profile(client, user_creation):

    client.force_login(user_creation)
    user = user_creation

    response = check_access_logined_user(client, user_creation, f'/users/{user.id}/delete/', 'user/delete_confirmation.html')
    assert response.context['user'] == user


def test_user_delete_another_profile(client, user_creation):

    client.force_login(user_creation)
    user2 = User.objects.create(username='Another_User', password='12345qqQ!')
    url = f'/users/{user2.id}/delete/'

    response = client.get(url)

    assert response.status_code == 302
    assert '/users/' in response.url


def test_user_update(client, user_creation):

    client.force_login(user_creation)
    user = user_creation
    url = f'/users/{user.id}/update/'
    new_query_data = {
        'username': 'Updated_user',
        'password1': '12345qqQ!',
        'password2': '12345qqQ!'
    }
    response = client.post(url, new_query_data)

    assert response.status_code == 302
    assert '/users/' in response.url
    assert User.objects.filter(id=user.id, username='Updated_user').exists()


def test_user_delete(client, user_creation):

    client.force_login(user_creation)
    user = user_creation
    url = f'/users/{user.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/users/' in response.url
    assert not User.objects.filter(id=user.id).exists()


def test_user_task_connection(client, user_creation, task_creation, status_creation):

    client.force_login(user_creation)
    user = user_creation
    task = Task.objects.create(name='test_task', author=user_creation, performer=user_creation, status=status_creation)

    url = f'/users/{user.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/users/' in response.url
    assert User.objects.filter(id=user.id).exists()



