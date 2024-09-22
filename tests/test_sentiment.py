import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import SentimentRequest

client = TestClient(app)

# Sample Arabic comments for testing
FAKE_COMMENTS = [
    "هذا الحدث كان رائعًا!",
    "لم أستمتع بالتجربة.",
    "كان جيدًا، لكن لا شيء مميز."
]

FAKE_EVENT_IDS = [1, 2, 3]

def test_sentiment_success():
    response = client.post("/sentiment", json={
        "comments": FAKE_COMMENTS,
        "event_id": FAKE_EVENT_IDS
    })

    assert response.status_code == 200
    assert isinstance(response.json(), dict)  # Ensure it returns a dictionary
    assert len(response.json()) == len(FAKE_EVENT_IDS)  # Should return ratings for each event ID

def test_sentiment_missing_json():
    response = client.post("/sentiment", json=None)
    assert response.status_code == 400
    assert response.json() == {"detail": "Please provide JSON data."}

def test_sentiment_empty_input():
    response = client.post("/sentiment", json={
        "comments": [],
        "event_id": []
    })
    
    assert response.status_code == 200
    assert response.json() == {}  # Assuming it returns an empty dict for no comments
