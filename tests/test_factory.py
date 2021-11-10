from flask.wrappers import Response
from fruitpal import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    rv = client.get('/hello')
    assert rv.data == b'hello world!'


def test_hello_pricecheck(client):
    rv = client.get('/hello/pricecheck?quantity=2&price=2&commodity=mango')
    assert  b'VARIABLE_PRICE' in rv.data
    assert  b'COUNTRY' in rv.data
    
    