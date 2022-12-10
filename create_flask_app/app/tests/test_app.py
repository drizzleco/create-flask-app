from client import client


def test_hello(client):
    resp = client.get("/hello")
    assert resp.data == b"hello"
