from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    """
    Model for validating chatbot request.
    """
    question: str