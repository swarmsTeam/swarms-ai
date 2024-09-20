from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chatbot_endpoint():
    response = client.post("/chatbot", json={"question": "Tell me about upcoming events at Mansoura University."})
    assert response.status_code == 200
    assert "AI Workshop" in response.json()['response']

def test_chatbot_invalid_input():
    response = client.post("/chatbot", json={})
    assert response.status_code == 422  # Validation error for missing 'question'