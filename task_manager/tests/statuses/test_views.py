from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user
from task_manager.user.models import User
from task_manager.status.forms import StatusForm
from task_manager.status.models import Status


def test_statuses_view_anonymous(client):
    check_access_anonymous(client, '/statuses/')


def test_statuses_view_logined_user(client, user_creation):
    check_access_logined_user(client, user_creation, '/statuses/', 'status/statuses.html')



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
    new_query_data = {
        'name': 'Updated'
    }
    response = client.post(url, new_query_data)

    assert response.status_code == 302
    assert '/statuses/' in response.url
    assert Status.objects.filter(id=status.id, name='Updated').exists()