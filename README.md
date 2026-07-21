# Task 1 — Dockerized Web Application

CodSoft DevOps Internship — Task 1 submission.

A small Flask web app (profile card + JSON status endpoint), containerized with Docker.

## Task Checklist

- [x] Install Docker and create a containerized web application
- [x] Write a Dockerfile to package the application and its dependencies
- [x] Build and run the Docker image locally
- [x] Verify the application is accessible through the browser
- [ ] Bonus: Push the Docker image to Docker Hub (commands below)

## Project Structure

```
task1-dockerized-webapp/
├── app.py                 # Flask app (routes: /, /about, /api/status)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml      # optional one-command run
├── templates/
│   ├── index.html
│   └── about.html
└── static/css/style.css
```

## Run Locally (without Docker)

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Visit http://127.0.0.1:5000

## Run With Docker

```bash
# 1. Build the image
docker build -t task1-dockerized-webapp .

# 2. Run the container
docker run -d -p 5000:5000 --name task1-app task1-dockerized-webapp

# 3. Verify
curl http://localhost:5000/api/status
# or open http://localhost:5000 in your browser

# 4. Stop & remove when done
docker stop task1-app && docker rm task1-app
```

Or with docker-compose (does build + run in one step):
```bash
docker compose up --build
```

## Bonus: Push to Docker Hub

```bash
docker login
docker tag task1-dockerized-webapp <your-dockerhub-username>/task1-dockerized-webapp:latest
docker push <your-dockerhub-username>/task1-dockerized-webapp:latest
```

Anyone can then run it with just:
```bash
docker run -p 5000:5000 <your-dockerhub-username>/task1-dockerized-webapp:latest
```

## What the Dockerfile Does (for the video explanation)

1. Starts from a lightweight official `python:3.12-slim` base image
2. Copies `requirements.txt` first and installs dependencies — this layer gets cached, so rebuilding after a code change doesn't reinstall packages every time
3. Copies the rest of the application code
4. Runs the app with **Gunicorn** (a production WSGI server) instead of Flask's built-in dev server — this is the same pattern used in real deployments

## Endpoints

| Route | Description |
|---|---|
| `/` | Profile card home page |
| `/about` | About this app |
| `/api/status` | JSON health check — `{"status": "running", ...}` |
