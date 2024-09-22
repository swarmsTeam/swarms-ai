import pytest
from app.main import app
from fastapi.testclient import TestClient
from app.models import RecommendationRequest
from unittest.mock import patch

client = TestClient(app)

# Sample fallback user and event data
FAKE_USERS_DATA = [
    {
    'id': 1, 
    'college_name': 'Engineering', 
    'user_skill': 'machine learning', 
    'user_interests': 'AI, tech'
    },
    {
    'id': 2, 
    'college_name': 'Business', 
    'user_skill': 'finance', 
    'user_interests': 'economics, startups'
    }
]

FAKE_EVENTS_DATA = [
    {'event_id': 1, 
    'name': 'Tech Talk', 
    'description': 'AI advancements', 
    'start_date': '2024-09-15', 
    'end_date': '2024-09-16', 
    'type': 'Talk', 
    'status': 'upcoming', 
    'category': 'tech'
    },
    {
    'event_id': 2, 
    'name': 'Music Fest', 
    'description': 'Live concert by a famous artist', 
    'start_date': '2024-09-20', 
    'end_date': '2024-09-21', 
    'type': 'Concert', 
    'status': 'upcoming', 
    'category': 'music'
    }
]

# Mocking requests.get to return our fake data
def mock_get(url, *args, **kwargs):
    if "users" in url:
        return MockResponse(FAKE_USERS_DATA, 200)
    elif "events" in url:
        return MockResponse(FAKE_EVENTS_DATA, 200)
    return MockResponse(None, 404)

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"HTTP {self.status_code} error")

# Test Cases
@pytest.fixture(autouse=True)
def mock_requests_get(monkeypatch):
    monkeypatch.setattr("requests.get", mock_get)

def test_get_recommendations_success():
    response = client.post("/recommendations", json={"user_id": [1, 2]})
    assert response.status_code == 200
    assert len(response.json()) == 2  # Should return 2 users
    assert response.json()[0]["user_id"] == 1  # Check first user ID
    assert isinstance(response.json()[0]["event_id"], list)  # Ensure event_ids are in list

def test_get_recommendations_user_not_found():
    response = client.post("/recommendations", json={"user_id": [999]})  # Non-existing user
    assert response.status_code == 200
    assert len(response.json()) == 1  # Should return one user
    assert response.json()[0]["user_id"] == 999  # Check user ID
    assert response.json()[0]["event_id"] == []  # No events for non-existing user

def test_get_recommendations_empty_input():
    response = client.post("/recommendations", json={"user_id": []})
    assert response.status_code == 200
    assert response.json() == []  # Should return an empty list

def test_get_recommendations_invalid_input():
    response = client.post("/recommendations", json={"user_id": "invalid"})
    assert response.status_code == 422  # Unprocessable Entity