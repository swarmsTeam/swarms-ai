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
curl -X POST http://localhost:5000/sentiment \
-H "Content-Type: application/json" \
-d '{
    "event_id": [1, 1, 2],
    "comments": ["الايفنت كان روعة وكل حاجة كانت قمة في الجمال", "روعة", "مش حلو خالص"]
}'
```

### Response

The response will include the star ratings for each unique `event_id` based on the sentiments of the associated comments.

- **Success (200)**:

```json
{"1":2.5,"2":2.5}
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
