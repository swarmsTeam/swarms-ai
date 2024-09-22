import pytest
from fastapi.testclient import TestClient
from app.main import app  # Update with your actual import path for the app
from app.models import ChatbotRequest

client = TestClient(app)

# Sample questions for testing
SAMPLE_QUESTIONS = [
    "What events are happening this week?",
    "Tell me about the Tech Talk event.",
    "Where can I find information about volunteering?",
]

# Test Cases
def test_chatbot_success():
    for question in SAMPLE_QUESTIONS:
        response = client.post("/chatbot", json={"question": question})
        assert response.status_code == 200
        assert "response" in response.json()  # Ensure response contains a key "response"

def test_chatbot_empty_question():
    response = client.post("/chatbot", json={"question": ""})
    assert response.status_code == 400  # Bad request for empty question
    assert response.json() == {'detail': 'Question cannot be empty.'}

def test_chatbot_invalid_input():
    response = client.post("/chatbot", json={"question": 123})  # Invalid question type
    assert response.status_code == 422  # Unprocessable Entity for invalid input

