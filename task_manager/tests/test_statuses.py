
from task_manager.status.models import Status
from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user


def test_statuses_main_view_anonymous(client):
    check_access_anonymous(client, '/statuses/')


def test_statuses_create_view_anonymous(client):
    check_access_anonymous(client, '/statuses/create/')


def test_statuses_update_view_anonymous(client, status_creation):

    status = status_creation
    check_access_anonymous(client, f'/statuses/{status.id}/update/')


def test_statuses_delete_view_anonymous(client, status_creation):

    status = status_creation
    check_access_anonymous(client, f'/statuses/{status.id}/delete/')


def test_statuses_main_view_logined_user(client, user_creation):
    response = check_access_logined_user(client, user_creation, '/statuses/', 'status/statuses.html')
    assert 'statuses' in response.context


def test_statuses_create_view_logined_user(client, user_creation):
    response = check_access_logined_user(client, user_creation, '/statuses/create/', 'status/status_create.html')
    assert 'form' in response.context


def test_statuses_update_view_logined_user(client, user_creation, status_creation):

    status = status_creation
    response = check_access_logined_user(client, user_creation, f'/statuses/{status.id}/update/', 'status/status_update.html')
    assert response.context['status'] == status


def test_statuses_delete_view_logined_user(client, user_creation, status_creation):

    status = status_creation
    check_access_logined_user(client, user_creation, f'/statuses/{status.id}/delete/', 'status/delete_confirmation.html')



def test_status_create(client, user_creation):

    client.force_login(user_creation)
    query_data = {
        'name': 'Completed'
    }
    response = client.post('/statuses/create/', query_data)

    assert response.status_code == 302
    assert '/statuses/' in response.url
    assert Status.objects.filter(name='Completed').exists()


def test_status_update(client, user_creation, status_creation):

    client.force_login(user_creation)
    status = status_creation
    url = f'/statuses/{status.id}/update/'
    new_query_data = {
        'name': 'Updated'
    }
    response = client.post(url, new_query_data)

    assert response.status_code == 302
    assert '/statuses/' in response.url
    assert Status.objects.filter(id=status.id, name='Updated').exists()


def test_status_delete(client, user_creation, status_creation):

    client.force_login(user_creation)
    status = status_creation
    url = f'/statuses/{status.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/statuses/' in response.url
    assert not Status.objects.filter(id=status.id).exists()


def test_status_task_connection(client, user_creation, task_creation, status_creation):

    client.force_login(user_creation)
    status = status_creation
    task = task_creation

    url = f'/statuses/{status.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/statuses/' in response.url
    assert Status.objects.filter(id=status.id).exists()