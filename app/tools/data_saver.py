import json

class DataSaver:
    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def save_user_data(users):
        DataSaver.save_to_file(users, 'data/user_data.json')

    @staticmethod
    def save_event_data(events):
        DataSaver.save_to_file(events, 'data/event_data.json')