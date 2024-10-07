from fastapi.testclient import TestClient

from app.api.crud.task_crud import create_task, read_task
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hell, World!"}

########### TEST TASK_CRUD ##################

payload = {"title":"Gaming", "description":"Play SM64"}
route_response = {
        "title": "Gaming",
        "description": "Play SM64",
        "id": 1,
        # "created": "2024-08-12T10:30:40.927951"
    }

def test_create_task():
    response = client.post("/tasks/", json=payload)
    json = response.json()
    
    assert response.status_code == 201
    assert json["id"] == 1
    assert json["title"] == payload["title"]
    assert json["description"] == payload["description"]
    assert json["created"] != None

def test_read_task():
    response = client.get("/tasks/1")
    json = response.json()
    
    assert response.status_code == 200
    assert json["id"] == 1
    assert json["title"] == payload["title"]
    assert json["description"] == payload["description"]
    assert json["created"] != None