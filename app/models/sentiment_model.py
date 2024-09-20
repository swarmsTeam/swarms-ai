from pydantic import BaseModel
from typing import List

class SentimentRequest(BaseModel):
    """
    Model for validating sentiment analysis request.
    """
    comments: List[str]
    event_id: List[int]