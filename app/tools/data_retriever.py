import os
import requests
from dotenv import load_dotenv
from app.tools import DataLoader, DataSaver

# Load secret keys from environment variables
load_dotenv()
USERS_API = os.getenv('USERS_API')
EVENTS_API = os.getenv('EVENTS_API')

class DataRetriever:
    @staticmethod
    def fetch_data_from_api(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json().get("data", [])
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.ConnectionError:
            print("Connection error occurred. Check your internet connection.")
        except requests.Timeout:
            print("Request timed out.")
        except Exception as err:
            print(f"An error occurred: {err}")
        return None

    @staticmethod
    def get_users():
        users = DataRetriever.fetch_data_from_api(USERS_API)
        if users:
            DataSaver.save_user_data(users)
        else:
            users = DataLoader.load_fallback_users()
        return users

    @staticmethod
    def get_events():
        events = DataRetriever.fetch_data_from_api(EVENTS_API)
        if events:
            DataSaver.save_event_data(events)
        else:
            events = DataLoader.load_fallback_events()
        return events
