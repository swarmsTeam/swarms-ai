# Run the API locally

### 1. Install Docker and Docker Compose:

- Make sure you have [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your local machine.

### 2. Clone the Repository:

Clone the project repository to your local machine.

```bash
git clone https://github.com/swarmsTeam/swarms-ai.git
cd swarms-ai/sentiment-analysis/app
```

### 3. Build the Docker Image:

Run the following command to build the Docker image locally.

```bash
docker-compose build
```

This will read the `Dockerfile` and create a local image for the app.

### 4. Run the Docker Container:

After building the image, run the container using Docker Compose:

```bash
docker-compose up
```

This will start the Flask application on port `5000`. You should see logs in your terminal indicating the app is running.

### 5. Access the Application:

Open your web browser and navigate to `http://localhost:5000`. The Flask app should be up and running.

### 6. Stopping the Containers:

To stop the Docker containers, press `CTRL + C` in the terminal where `docker-compose` is running. If you want to stop it gracefully, use:

```bash
docker-compose down
```

### 7. Troubleshooting:
- If you encounter permission issues, try using `sudo` for Docker commands.
- Make sure you have all dependencies listed in `requirements.txt`.
