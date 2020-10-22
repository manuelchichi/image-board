from flask import url_for

def test_app_index(client):
    assert client.get(url_for('main.index')).status_code == 200

def test_app_login(client):
    assert client.get(url_for('auth.login')).status_code == 200