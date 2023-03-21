from app import app

def test_ping():
    client = app.test_client()
    response = client.get('/ping/')
    print(response.data)
    assert response.status_code == 200
    assert response.data == b"Pong!"
