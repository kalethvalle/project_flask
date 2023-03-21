import json
from app import app

def test_get_all_tasks():
    client = app.test_client()
    response = client.get('/api/task')
    assert response.status_code == 200
    tasks = json.loads(response.data)
    assert len(tasks) > 0
