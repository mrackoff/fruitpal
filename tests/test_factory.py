from fruitpal import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'hello world!'


def test_hello_pricecheck(client):
    response = client.get('/hello/pricecheck/1/2/mango')
    assert response.data == b'hello world!'