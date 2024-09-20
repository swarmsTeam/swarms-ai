from fastapi import APIRouter, HTTPException
from app.services import process_chatbot_query
from app.models import ChatbotRequest

router = APIRouter()

# Chatbot endpoint
@router.post("/chatbot")
async def chatbot(query: ChatbotRequest):
    try:
        response = process_chatbot_query(query.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}") 