from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services import calculate_ratings
from app.models import SentimentRequest
import pandas as pd

# Create a router for sentiment-related endpoints
router = APIRouter()

@router.post("/sentiment")
async def sentiment(request_data: SentimentRequest = None):
    # Check if JSON data is provided
    if not request_data:
        raise HTTPException(status_code=400, detail="Please provide JSON data.")

    # Load the data from the JSON request
    data = pd.DataFrame({'event_id': request_data.event_id, 'description': request_data.description})

    # Ensure 'description' and 'event_id' columns exist
    if 'description' not in data.columns or 'event_id' not in data.columns:
        raise HTTPException(status_code=400, detail="Missing required columns: description, event_id")

    # Call the service to calculate the ratings
    ratings = calculate_ratings(data)

    return ratings