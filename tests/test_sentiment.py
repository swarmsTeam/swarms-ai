from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_sentiment_with_json():
    # Test case for valid JSON input
    response = client.post(
        "/sentiment",  # Update the endpoint path if needed
        json={"comments": ["This event was great!", "I didn't like it."], "event_id": [1, 1]}
    )
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, dict)  # The result should be a dictionary
    assert "1" in result  # Event ID 1 should be in the response
    
def test_sentiment_with_invalid_json():
    # Test case for invalid JSON input
    response = client.post(
        "/sentiment",
        json={"comments": ["Good"], "invalid_field": [1]}
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Missing required columns: comments, event_id"}

def test_sentiment_with_csv():
    # Test case for valid CSV input
    file_content = "comments,event_id\n'Good event',1\n'Bad event',1"
    response = client.post(
        "/sentiment",
        files={"file": ("test.csv", file_content, "text/csv")}
    )
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, dict)

def test_invalid_content_type():
    # Test case for unsupported content type
    response = client.post(
        "/sentiment",
        data="Unsupported content type"
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Please provide either a CSV file or JSON data."}