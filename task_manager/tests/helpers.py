from task_manager.user.models import User


def check_access_anonymous(client, url):
    
    response = client.get(url)
    
    assert response.status_code == 302
    assert '/login/' in response.url


def check_access_logined_user(client, url, template):

    user = User.objects.create_user(username='test_user', password='12345qqQ!')
    client.force_login(user)
    response = client.get(url)

    assert response.status_code == 200
    assert template in [t.name for t in response.templates]