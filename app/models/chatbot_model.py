from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    question: str