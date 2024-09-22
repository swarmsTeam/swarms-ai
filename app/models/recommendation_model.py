from pydantic import BaseModel
from typing import List

class RecommendationRequest(BaseModel):
    """
    Model for validating recommendation system request.
    """
    user_id: List[int]  # List of user_ids
