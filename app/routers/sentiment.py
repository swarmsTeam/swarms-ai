from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List
import pandas as pd
from app.services import calculate_ratings
from pydantic import BaseModel

# Create a router for sentiment-related endpoints
router = APIRouter()

class SentimentRequest(BaseModel):
    event_id: List[int]
    comments: List[str]

@router.post("/sentiment")
async def sentiment(request_data: SentimentRequest = None):
    # Check if JSON data is provided
    if not request_data:
        raise HTTPException(status_code=400, detail="Please provide JSON data.")

    # Load the data from the JSON request
    data = pd.DataFrame({'event_id': request_data.event_id, 'comments': request_data.comments})

    # Ensure 'comments' and 'event_id' columns exist
    if 'comments' not in data.columns or 'event_id' not in data.columns:
        raise HTTPException(status_code=400, detail="Missing required columns: comments, event_id")

    # Call the service to calculate the ratings
    ratings = calculate_ratings(data)

    return ratings