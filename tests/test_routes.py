from todo_app.database import Task

def test_create_task_status_code(client, create_response):
    assert create_response.status_code == 201

def test_create_task_title(client, create_response):
    data = create_response.get_json()
    assert data['title'] == 'Test Title'

def test_create_task_description(client, create_response):
    data = create_response.get_json()
    assert data['description'] == 'Test Description'

def test_get_tasks(client, session):
    for i in range(5):
        task = Task(title=f'test title # {i+1}', description=f'test desc # {i+1}')
        session.add(task)
    session.commit()
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 5
    assert data[0]['title'] == 'test title # 1'
    assert data[0]['description'] == 'test desc # 1'

def test_update_task(client, session):
    task = Task(title='test title for update', description='test description for update')
    session.add(task)
    session.commit()

    response = client.put(f'tasks/{task.id}', json={
        'title': 'updated title',
        'description': 'updated desc'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'updated title'
    assert data['description'] == 'updated desc'

def test_delete_task(client, session):
    task = Task(title='test title', description='test description')
    session.add(task)
    session.commit()

    response = client.delete(f'tasks/{task.id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Task deleted successfully'

    response = client.get(f'tasks/{task.id}')
    assert response.status_code == 404
