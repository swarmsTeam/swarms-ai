from transformers import pipeline
import pandas as pd
import json

# Load the pre-trained sentiment analysis model
MODEL = "CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"
pipe = pipeline("text-classification", model=MODEL)

def calculate_ratings(data: pd.DataFrame) -> pd.Series:
    """
    Calculate sentiment ratings based on comments and group them by event_id.
    
    Args:
        data (pd.DataFrame): Data containing 'comments' and 'event_id'.
    
    Returns:
        pd.Series: The star ratings grouped by event_id.
    """
    # Initialize score column
    data['score'] = None

    # Process each review and assign sentiment score
    for index, review in data.iterrows():
        sentiment = pipe(review['comments'])[0]
        score = sentiment['score']

        # Adjust score based on sentiment label
        if sentiment['label'] == 'negative':
            score = 1 - score
        elif sentiment['label'] == 'positive':
            score = score
        else:
            score = 0.5

        data.at[index, 'score'] = score

    # Group by event_id and calculate the total score and review count
    grouped = data.groupby('event_id').agg({"score": ["sum", "count"]})
    grouped.columns = ["total_score", "length"]

    # Calculate star rating
    grouped['star_rating'] = grouped['total_score'] / (grouped['length'] / 5)
    return grouped['star_rating']