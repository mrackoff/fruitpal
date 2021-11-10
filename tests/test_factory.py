from flask.wrappers import Response
from fruitpal import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    rv = client.get('/hello')
    assert rv.data == b'hello world!'

    
    