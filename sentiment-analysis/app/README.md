# Run the API locally

## 1. Install Docker and Docker Compose:

- Make sure you have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your local machine.

## 2. Clone the Repository:

Clone the project repository to your local machine.

```bash
git clone https://github.com/swarmsTeam/swarms-ai.git
cd swarms-ai/sentiment-analysis/app
```

## 3. Build the Docker Image:

Run the following command to build the Docker image locally.

```bash
docker-compose build
```

This will read the `Dockerfile` and create a local image for the app.

## 4. Run the Docker Container:

After building the image, run the container using Docker Compose:

```bash
docker-compose up
```

This will start the Flask application on port `5000`. You should see logs in your terminal indicating the app is running.

## 5. Access the Application:

The EVNTO Sentiment Analysis API allows users to submit event-related comments in either **CSV** or **JSON** format, and the API will return an overall rating for each unique `event_id`.

The API leverages a pre-trained model to perform sentiment analysis on comments and computes a star rating based on the sentiment of those comments.

### Endpoints

### 1. `/sentiment`

This endpoint accepts a **POST** request with event comments in **JSON** or **CSV** format and returns an overall star rating for each event.

- **URL**: `/sentiment`
- **Method**: `POST`
- **Content-Type**: `application/json` or `text/csv`

### Request Parameters

- **event_id**: (string) A unique identifier for each event.
- **comment**: (string) The comment or review text associated with the event.

### Example Request (JSON)

```bash
curl -X POST http://localhost:5000/sentiment \\
-H "Content-Type: application/json" \\
-d '{
  "data": [
    {"event_id": "123", "comment": "The event was fantastic, very engaging!"},
    {"event_id": "123", "comment": "Could have been more organized."},
    {"event_id": "124", "comment": "Had a great time, well done!"},
    {"event_id": "124", "comment": "Not worth the time."}
  ]
}'
```

### Example Request (CSV)

To send a CSV file, you can use a tool like Postman, or you can upload it programmatically.

Here’s an example using `curl`:

```bash
curl -X POST http://localhost:5000/sentiment \\
-H "Content-Type: text/csv" \\
--data-binary @comments.csv
```

In this example, `comments.csv` should look like:

```
event_id,comment
123,The event was fantastic, very engaging!
123,Could have been more organized.
124,Had a great time, well done!
124,Not worth the time.
```

### Response

The response will include the star ratings for each unique `event_id` based on the sentiments of the associated comments.

- **Success (200)**:

```json
{
  "ratings": {
    "123": 4.2,
    "124": 3.5
  }
}
```

- **Error (400)**: If there is an issue with the request, such as missing fields or incorrect formatting.

```json
{
  "error": "Invalid input format."
}
```

## 6. Stopping the Containers:

To stop the Docker containers, press `CTRL + C` in the terminal where `docker-compose` is running. If you want to stop it gracefully, use:

```bash
docker-compose down
```

## 7. Troubleshooting:

- If you encounter permission issues, try using `sudo` for Docker commands.
- Make sure you have all dependencies listed in `requirements.txt`.
