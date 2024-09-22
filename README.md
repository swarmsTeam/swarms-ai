# AI-Components for EVNTO app

## Overview
This project is part of the **EVNTO** app aimed at improving engagement for Mansoura University students by providing them with useful AI tools such as sentiment analysis, a chatbot, and a cold start recommendation system. It focuses on leveraging AI to help students discover relevant events and volunteer opportunities, and provides event organizers with valuable insights into user sentiment.

The system includes the following components:

1. **Sentiment Analysis**: Analyses user comments to provide event organizers with star ratings based on the sentiment of the reviews.
2. **Chatbot**: A question-answering chatbot designed to assist users in finding information about events using Google Generative AI.
3. **Cold Start Recommendation System**: Recommends events to new users or users with limited interaction history using a vectorized embedding-based system.


## Installation and Setup

### Environment Variables
The following environment variables need to be set:
- `GOOGLE_API_KEY`: API key for Google Generative AI used in the chatbot.
- `USERS_API`: API to fetch users data from evnto database.
- `EVENTS_API`: API to fetch events data from evnto database.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/swarmsTeam/swarms-ai.git
   cd swarms-ai
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the app at `http://127.0.0.1:8000`.

### Docker Setup
The app can also be containerized using Docker.

1. Build the Docker image:
   ```bash
   docker build -t evnto-ai-app .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 evnto-ai-app
   ```

## API Endpoints

### 1. Sentiment Analysis

**Endpoint**: `POST /sentiment`

**Request**:
```json
{
    "event_id": [1, 2],
    "description": ["الايفنت كان جميل جدا", "التنظيم كان عادي على عكس المتوقع"]
}
```

**Response**:
```json
{
    "1": 4.5,  // Average star rating for event_id 1
    "2": 2.5   // Average star rating for event_id 2
}
```

**Description**: Analyses user comments and returns the average star rating for each event based on the sentiment score of the comments.

### 2. Chatbot

**Endpoint**: `POST /chatbot`

**Request**:
```json
{
    "question": "What events are happening this week?"
}
```

**Response**:
```json
{
    "response": "There are two events happening this week: AI Workshop and Python Bootcamp."
}
```

**Description**: Processes the user's question and provides information about events (handle multiple languages).

### 3. Cold Start Recommendation System

**Endpoint**: `POST /recommendations`

**Request**:
```json
{
    "user_id": [1]
}
```

**Response**:
```json
{
    "user_id": 1,
    "event_id": [1, 5, 7]  // List of event_ids recommended for the user
}
```

**Description**: Recommends events to users based on their profile, interests, and skills using embeddings.

## Data Retrieval and Preprocessing

This project retrieves two JSON files from the database: one for **events** and one for **users**.

### Event Data (`events.json`):
- Relevant columns: `event_id`, `name`, `description`, `start_date`, `end_date` `type`, `status`, `category`, `rating`, `goals`
- The data is processed by filtering out the required columns and ignoring the rest.

### User Data (`users.json`):
- Relevant columns: `user_id`, `college_name`, `user_skills`, `user_interests`
- This data is used for building user profiles in the recommendation system.

**Example Code to Fetch and Preprocess Data**:
```python
import pandas as pd

def preprocess_json(json_data, required_columns):
    df = pd.DataFrame(json_data['data'])
    return df[required_columns]

# Example usage
events_data = fetch_data_from_api(events_url)
preprocessed_events = preprocess_json(events_data, ["event_id", "name", "description", "type", "category", "rating", "goals"])
```

## Testing

This project uses **pytest** for testing. The test cases cover each AI component.

### Running Tests

1. Install test dependencies:
   ```bash
   pip install pytest
   ```

2. Run tests:
   ```bash
   python -m pytest tests/
   ```

### Test Coverage

The tests ensure the APIs function as expected for both successful and erroneous inputs.

- **Sentiment Analysis**:
    - Tests check for valid input, missing columns, and empty comments.
    - Expected star ratings are verified.

- **Chatbot**:
    - Tests verify valid questions, empty questions, and exception handling.
    - Mocking is used to simulate error scenarios.

- **Cold Start Recommendation**:
    - Tests ensure that users receive appropriate event recommendations.
    - Scenarios with missing user profiles are also handled.

**Example Test (Sentiment Analysis)**:
```python
def test_sentiment_analysis():
    response = client.post("/sentiment", json={
        "event_id": [1],
        "comments": ["Fantastic event!"]
    })
    assert response.status_code == 200
    assert response.json()[1] == 5.0  # Check that the sentiment rating is as expected
```

## Future Enhancements

### **Dynamic Event Scheduling**:
   - **What it does**: A system that analyses user availability and preferences and suggests the best times for attending or hosting events.
   - **How to build**: Use time-series data from users' past attendance and availability calendars, optimizing scheduling through a reinforcement learning approach.

### **Event Success Prediction**:
   - **What it does**: Predict the success of future events based on past attendance, feedback, and sentiment analysis.
   - **How to build**: Train a model using data from past events (attendance rates, reviews, engagement metrics) to forecast the potential success or failure of upcoming events.

### **Social Network Analysis for Teams**:
   - **What it does**: Analyze interactions between users (team members, volunteers, mentors) to detect influential people or bottlenecks in communication.
   - **How to build**: Use graph-based machine learning methods to map out social relationships and find patterns that could lead to improved team dynamics.


## Contributing
We welcome contributions to this project! Please see the [`CONTRIBUTING.md`](https://github.com/swarmsTeam/swarms-ai/blob/main/CONTRIBUTING.md) file  for guidelines on how to submit pull requests.

## License 
This project is licensed under the MIT License (see [`LICENSE`](https://github.com/swarmsTeam/swarms-ai/blob/main/LICENSE) for details).
