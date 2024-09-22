# router.py
from fastapi import APIRouter, HTTPException
from app.services import RecommendationService
from app.models import RecommendationRequest

router = APIRouter()

@router.post("/recommendations")
async def get_recommendations(request_data: RecommendationRequest):
    try:
        user_ids = request_data.user_id
        recommendations = RecommendationService.get_recommendations_for_users(user_ids)
        return recommendations
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching recommendations: {str(e)}")
