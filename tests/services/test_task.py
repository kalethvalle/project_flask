from app import app
import json

def test_get_all_tasks():
    client = app.test_client()
    response = client.get('/api/task')
    tasks = json.loads(response.data)
    assert response.status_code == 200
    assert len(tasks) > 0

def test_create_task():
    client = app.test_client()
    data = { 'title': 'title test', 'task_description': 'title description' }
    response = client.post('/api/task', json=data)
    task = json.loads(response.data)
    assert response.status_code == 200
    assert task['title'] == 'title test'

def test_create_error_title_task():
    client = app.test_client()
    data = { 'tittle': 'title test', 'task_description': 'title description' }
    response = client.post('/api/task', json=data)
    task = json.loads(response.data)
    assert response.status_code == 400
    assert task['Error'] == 'Error creatting task, title is required'

def test_create_error_task_description_task():
    client = app.test_client()
    data = { 'title': 'title test', 'description': 'title description' }
    response = client.post('/api/task', json=data)
    task = json.loads(response.data)
    assert response.status_code == 400
    assert task['Error'] == 'Error creatting task, description is required'

def test_get_by_id_tasks():
    client = app.test_client()
    response = client.get('/api/task/20')
    tasks = json.loads(response.data)
    assert response.status_code == 200
    assert tasks == {'created': 'Mon, 20 Mar 2023 21:34:12 GMT', 'id': 20, 'task_description': 'description 7', 'title': 'task 7'}

def test_get_by_id_not_found_task():
    client = app.test_client()
    response = client.get('/api/task/112350')
    tasks = json.loads(response.data)
    assert response.status_code == 404
    assert tasks['Error'] == ' Error getting by id task'

def test_update_task():
    client = app.test_client()
    response = client.post('/api/task', json={'title': 'Task 1', 'task_description': 'This is Task 1'})
    id = json.loads(response.data)['id']
    response = client.patch(f'/api/task/{id}', json={'title': 'Task 2', 'task_description': 'This is Task 2'})
    task = json.loads(response.data)
    assert response.status_code == 200
    assert task['title'] == 'Task 2'

def test_update_error_task():
    client = app.test_client()
    response = client.patch('/api/task/254631', json={'title': 'Task 2', 'task_description': 'This is Task 2'})
    task = json.loads(response.data)
    assert response.status_code == 500
    assert task['Error'] == 'Error updatting task'