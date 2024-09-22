import torch
import pandas as pd
import numpy as np
from app.tools import DataRetriever
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

# Transformer model and tokenizer are initialized only once.
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

class RecommendationService:
    @staticmethod
    def filter_active_events(events):
        events_df = pd.DataFrame(events)
        return events_df[events_df['status'] != 'ended']

    @staticmethod
    def generate_event_embeddings(events_df):
        combined_features = events_df['type'] + " " + events_df['description'] + " " + events_df['category']
        inputs = tokenizer(combined_features.tolist(), return_tensors='pt', padding=True, truncation=True)

        with torch.no_grad():
            event_embeddings = model(**inputs).last_hidden_state.mean(dim=1)
        return event_embeddings.cpu().numpy()

    @staticmethod
    def recommend_events_for_user(user, event_embeddings, events_df):
        user_profile_text = user['user_skill'] + " " + user['user_interests']
        inputs = tokenizer([user_profile_text], return_tensors='pt', padding=True, truncation=True)

        with torch.no_grad():
            user_embedding = model(**inputs).last_hidden_state.mean(dim=1)
        user_embedding = user_embedding.cpu().numpy()

        similarity_scores = cosine_similarity(user_embedding, event_embeddings)
        recommended_event_indices = similarity_scores.argsort()[0][::-1]

        return events_df.iloc[recommended_event_indices[:5]]['event_id'].values.tolist()

    @staticmethod
    def get_recommendations_for_users(user_ids):
        users = DataRetriever.get_users()
        events = DataRetriever.get_events()
        events_df = RecommendationService.filter_active_events(events)

        event_embeddings = RecommendationService.generate_event_embeddings(events_df)

        recommendations = []
        for user_id in user_ids:
            user = next((u for u in users if u['id'] == user_id), None)
            if not user:
                recommendations.append({"user_id": user_id, "event_id": []})
                continue
            recommended_events = RecommendationService.recommend_events_for_user(user, event_embeddings, events_df)
            recommendations.append({"user_id": user_id, "event_id": recommended_events})

        return recommendations