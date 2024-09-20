from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List
import pandas as pd
from services.sentiment_service import calculate_ratings
from pydantic import BaseModel
from io import StringIO

# Create a router for sentiment-related endpoints
router = APIRouter()

class SentimentRequest(BaseModel):
    comments: List[str]
    event_id: List[int]

@router.post("/sentiment")
async def sentiment(file: UploadFile = File(None), request_data: SentimentRequest = None):
    # Check if either file or JSON body is provided
    if not file and not request_data:
        raise HTTPException(status_code=400, detail="Please provide either a CSV file or JSON data.")

    # Load the data from CSV or JSON
    try:
        if file:
            contents = await file.read()
            data = pd.read_csv(StringIO(contents.decode('utf-8')))
        else:
            data = pd.DataFrame({'comments': request_data.comments, 'event_id': request_data.event_id})

        # Ensure 'comments' and 'event_id' columns exist
        if 'comments' not in data.columns or 'event_id' not in data.columns:
            raise HTTPException(status_code=400, detail="Missing required columns: comments, event_id")
        
        # Call the service to calculate the ratings
        ratings = calculate_ratings(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {str(e)}")

    return ratings.to_dict()