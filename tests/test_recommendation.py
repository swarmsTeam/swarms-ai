import pytest
from app.main import app
from fastapi.testclient import TestClient
from app.models import RecommendationRequest

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

# Mock DataLoader to provide fallback data
class MockDataLoader:
    @staticmethod
    def load_fallback_users():
        return FAKE_USERS_DATA

    @staticmethod
    def load_fallback_events():
        return FAKE_EVENTS_DATA

# Test Cases
@pytest.fixture(autouse=True)
def override_data_loader(monkeypatch):
    monkeypatch.setattr("app.data_loader.DataLoader", MockDataLoader)

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

def test_get_recommendations_api_error():
    # Simulate API error by providing a wrong URL or causing a failure in the fetch function
    # Here we could modify the fetch_data_from_api method temporarily for this test or
    # mock the requests.get call to raise an exception.
    response = client.post("/recommendations", json={"user_id": [1, 2]})
    assert response.status_code == 200  # Should still return valid fallback data
    assert len(response.json()) == 2  # Check that fallback data is returned
