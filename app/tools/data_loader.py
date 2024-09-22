import json
import os

class DataLoader:
    @staticmethod
    def load_fallback_users():
        users_file_path = os.path.join("data", "users_data.json")
        with open(users_file_path, "r") as file:
            users_data = json.load(file)
        return users_data

    @staticmethod
    def load_fallback_events():
        events_file_path = os.path.join("data", "events_data.json")
        with open(events_file_path, "r") as file:
            events_data = json.load(file)
        return events_data