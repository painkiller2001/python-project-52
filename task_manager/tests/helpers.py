

def check_access_anonymous(client, url):
    
    response = client.get(url)
    
    assert response.status_code == 302
    assert '/login/' in response.url


def check_access_logined_user(client, user, url, template):

    client.force_login(user)
    response = client.get(url)

    assert response.status_code == 200
    assert template in [t.name for t in response.templates]

    return response