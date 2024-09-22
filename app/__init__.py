from fastapi import FastAPI
from .routers import sentiment, chatbot, recommendation

# Initialize FastAPI app
app = FastAPI()

# Include the routers for different components
app.include_router(sentiment.router)
app.include_router(chatbot.router)
app.include_router(recommendation.router)
