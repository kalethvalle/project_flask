import json
import unittest
from app import app

def test_get_all_tasks():
    client = app.test_client()
    response = client.get('/api/task')
    assert response.status_code == 200
    tasks = json.loads(response.data)
    assert len(tasks) > 0

# class TestAPI(unittest.TestCase):
#     def setUp(self):
#         self.client = app.test_client()
#         self.task = {'title': 'Task 1', 'task_description': 'This is Task 1'}

#     def test_create_task(self):
#         response = self.client.post('/api/task', json=self.task)
#         # data = json.loads(response.data)
#         self.assertEqual(response.status_code, 200)
#         # self.assertEqual(data, {'created': 'Tue, 21 Mar 2023 03:38:20 GMT', 'id': 22, 'task_description': 'This is Task 1', 'tittle': 'Task 1'})

#     def test_get_all_tasks(self):
#         response = self.client.get('/api/task')
#         data = json.loads(response.data)
#         self.assertEqual(response.status_code, 200)
#         # self.assertEqual(len(data), 1)

#     # def test_update_task(self):
#     #     new_task = {'title': 'Task 2', 'description': 'This is Task 2'}
#     #     response = self.client.post('/tasks', json=self.task)
#     #     id = json.loads(response.data)['id']
#     #     response = self.client.put(f'/tasks/{id}', json=new_task)
#     #     data = json.loads(response.data)
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertEqual(data['message'], 'Task updated successfully')


# if __name__ == '__main__':
#     unittest.main()
