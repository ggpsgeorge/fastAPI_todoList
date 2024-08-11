from fastapi.testclient import TestClient
from datetime import datetime

from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hell, World!"}

def test_create_task():
    response = client.post("/tasks/", json={
        "title":"Gaming", "description":"Play Super Mario 64"
    })

    json = response.json()
    
    assert response.status_code == 200
    assert json["id"] == 1
    assert json["title"] == "Gaming"
    assert json["description"] == "Play Super Mario 64"
    assert json["created"] != None

def test_read_task():
    response = client.get("/tasks/1")
    json = response.json()
    
    assert response.status_code == 200
    assert json["id"] == 1
    assert json["title"] == "Gaming"
    assert json["description"] == "Play Super Mario 64"
    assert json["created"] != None