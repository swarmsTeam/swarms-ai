import pandas as pd
from transformers import pipeline

# Load the pre-trained sentiment analysis model
MODEL = "CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"
pipe = pipeline("text-classification", model=MODEL)

def rating_pipeline(data, comments, group):
    # Initialize score column
    data['score'] = None

    # Process each review
    for index, review in data.iterrows():
        sentiment = pipe(review[comments])[0]
        score = sentiment['score']
        
        # Adjust score based on sentiment label
        if sentiment['label'] == 'negative':
            score = 1 - score
        else:
            score = 0.5
        
        # Assign the score
        data.at[index, 'score'] = score

    # Group by event ID and calculate the total score and count of reviews
    grouped = data.groupby(group).agg({"score": ["sum", "count"]})
    grouped.columns = ["total_score", "length"]

    # Calculate star rating
    grouped['star_rating'] = grouped['total_score'] / (grouped['length'] / 5)

    return grouped['star_rating']