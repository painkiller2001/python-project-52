from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user
from task_manager.user.models import User
from task_manager.status.forms import StatusForm
from task_manager.status.models import Status


def test_statuses_view_anonymous(client):
    check_access_anonymous(client, '/statuses/')


def test_statuses_view_logined_user(client, db):
    check_access_logined_user(client, '/statuses/', 'status/statuses.html')



def test_status_create(client, db):
    user = User.objects.create_user(username='test_user', password='12345q!')
    client.force_login(user)
    query_data = {
        'name': 'Completed'
    }
    response = client.post('/statuses/create/', query_data)

    assert response.status_code == 302
    assert '/statuses/' in response.url
    assert Status.objects.filter(name='Completed').exists()