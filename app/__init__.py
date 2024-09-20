from fastapi import FastAPI
from app.routers import sentiment, chatbot, recommendation

# Initialize FastAPI app
app = FastAPI()

# Include the routers for different components
app.include_router(sentiment.router, prefix="/api/v1")
app.include_router(chatbot.router, prefix="/api/v1")
app.include_router(recommendation.router, prefix="/api/v1")
