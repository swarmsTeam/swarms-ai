from fastapi import FastAPI
from app.routers import sentiment, chatbot, recommendation

# Initialize the FastAPI app
app = FastAPI(
    title="EVNTO AI",
    description="API for the EVNTO app which includes sentiment analysis, chatbot, and recommendation system",
    version="1.0.0"
)

# Include the routers for the API endpoints
app.include_router(sentiment.router, tags=["Sentiment Analysis"])
app.include_router(chatbot.router, tags=["Chatbot"])
#app.include_router(recommendation.router, tags=["Recommendation System"])

# Root endpoint for health check
@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "EVNTO AI is running!"}
