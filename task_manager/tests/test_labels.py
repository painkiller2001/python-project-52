from task_manager.label.models import Label
from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user


def test_labels_main_view_anonymous(client):
    check_access_anonymous(client, '/labels/')


def test_labels_create_view_anonymous(client):
    check_access_anonymous(client, '/labels/create/')


def test_labels_update_view_anonymous(client, label_creation):

    label = label_creation
    check_access_anonymous(client, f'/labels/{label.id}/update/')


def test_labels_delete_view_anonymous(client, label_creation):

    label = label_creation
    check_access_anonymous(client, f'/labels/{label.id}/delete/')


def test_labels_main_view_logined_user(client, user_creation):
    response = check_access_logined_user(client, user_creation, '/labels/', 'label/labels.html')
    assert 'labels' in response.context


def test_labels_create_view_logined_user(client, user_creation):
    response = check_access_logined_user(client, user_creation, '/labels/create/', 'label/label_create.html')
    assert 'form' in response.context


def test_labels_update_view_logined_user(client, user_creation, label_creation):

    label = label_creation
    response = check_access_logined_user(client, user_creation, f'/labels/{label.id}/update/', 'label/label_update.html')
    assert response.context['label'] == label


def test_labels_delete_view_logined_user(client, user_creation, label_creation):

    label = label_creation
    check_access_logined_user(client, user_creation, f'/labels/{label.id}/delete/', 'label/delete_confirmation.html')


def test_label_create(client, user_creation):

    client.force_login(user_creation)
    query_data = {
        'name': 'Test_label'
    }
    response = client.post('/labels/create/', query_data)

    assert response.status_code == 302
    assert '/labels/' in response.url
    assert Label.objects.filter(name='Test_label').exists()


def test_label_update(client, user_creation, label_creation):

    client.force_login(user_creation)
    label = label_creation
    url = f'/labels/{label.id}/update/'
    new_query_data = {
        'name': 'Updated_test_label'
    }
    response = client.post(url, new_query_data)

    assert response.status_code == 302
    assert '/labels/' in response.url
    assert Label.objects.filter(id=label.id, name='Updated_test_label').exists()


def test_label_delete(client, user_creation, label_creation):

    client.force_login(user_creation)
    label = label_creation
    url = f'/labels/{label.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/labels/' in response.url
    assert not Label.objects.filter(id=label.id).exists()


def test_label_task_connection(client, user_creation, task_creation, label_creation):

    client.force_login(user_creation)
    label = label_creation
    task = task_creation
    task.labels.add(label)

    url = f'/labels/{label.id}/delete/'

    response = client.post(url)

    assert response.status_code == 302
    assert '/labels/' in response.url
    assert Label.objects.filter(id=label.id).exists()