from task_manager.tests.helpers import check_access_anonymous, check_access_logined_user


def test_statuses_view_anonymous(client):
    check_access_anonymous(client, '/statuses/')


def test_statuses_view_logined_user(client, db):
    check_access_logined_user(client, '/statuses/', 'status/statuses.html')