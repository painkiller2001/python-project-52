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
    check_access_logined_user(client, user_creation, '/labels/', 'label/labels.html')


def test_labels_create_view_logined_user(client, user_creation):
    check_access_logined_user(client, user_creation, '/labels/create/', 'label/label_create.html')


def test_labels_update_view_logined_user(client, user_creation, label_creation):

    label = label_creation
    check_access_logined_user(client, user_creation, f'/labels/{label.id}/update/', 'label/label_update.html')


def test_labels_delete_view_logined_user(client, user_creation, label_creation):

    label = label_creation
    check_access_logined_user(client, user_creation, f'/labels/{label.id}/delete/', 'label/delete_confirmation.html')