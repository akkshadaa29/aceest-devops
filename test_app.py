from app import app

def test_get_clients():
    client = app.test_client()
    response = client.get('/clients')
    
    assert response.status_code == 200


def test_add_client():
    client = app.test_client()
    
    response = client.post('/clients', json={
        "name": "Test User",
        "age": 25
    })

    assert response.status_code == 201
    assert b"Client added successfully" in response.data


def test_add_client_without_name():
    client = app.test_client()
    
    response = client.post('/clients', json={
        "age": 25
    })

    assert response.status_code == 400
