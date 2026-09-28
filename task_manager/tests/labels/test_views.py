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