

def check_access_anonymous(client, url):
    
    response = client.get(url)
    
    assert response.status_code == 302
    assert '/login/' in response.url


def check_access_logined_user(client, user, url, template):

    client.force_login(user)
    response = client.get(url)

    assert response.status_code == 200
    assert template in [t.name for t in response.templates]


# def check_create_get(client, url, user, template):

#     client.force_login(user)
#     response = client.get(url)

#     assert response.status_code == 200
#     assert template in [t.name for t in response.templates]


# def check_update_get(client, user_creation, status_creation):

#     client.force_login(user_creation)
#     status = status_creation
#     url = f'/statuses/{status.id}/update/'
#     response = client.get(url)

#     assert response.status_code == 200
#     assert template in [t.name for t in response.templates]


# def check_delete_get(client, user_creation, status_creation):

#     client.force_login(user_creation)
#     status = status_creation
#     url = f'/statuses/{status.id}/delete/'
#     response = client.get(url)

#     assert response.status_code == 200
#     assert template in [t.name for t in response.templates]