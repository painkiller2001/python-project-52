from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user


def test_labels_view_anonymous(client):
    check_access_anonymous(client, '/labels/')


def test_labels_view_logined_user(client, db):
    check_access_logined_user(client, '/labels/', 'label/labels.html')