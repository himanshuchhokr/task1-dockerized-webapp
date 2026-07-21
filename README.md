# Task 1 - Dockerized Web Application

## 👨‍💻 Developer
**Himanshu Chhokar**

## 📖 Project Description
This project is a Dockerized Python Flask web application developed as part of the CodSoft DevOps Internship.

The application displays a portfolio webpage and provides a REST API endpoint to verify that the application is running successfully.

---

## 🛠 Technologies Used

- Python
- Flask
- Gunicorn
- Docker
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
task1-dockerized-webapp/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── static/
├── templates/
└── README.md
```

---

## 🚀 How to Run

### Build Docker Image

```bash
docker build -t docker-webapp .
```

### Run Container

```bash
docker run -p 5001:5000 docker-webapp
```

---

## API Endpoint

```
GET /api/status
```

Example Response

```json
{
  "status": "running",
  "message": "Task 1 - Dockerized Web Application is live!"
}
```

---

## Docker Verification

```bash
docker ps
```

Container should be running successfully.

---

## Output

Application URL

```
http://localhost:5001
```

API URL

```
http://localhost:5001/api/status
```

---

## Internship

CodSoft DevOps Internship

Task 1 - Dockerized Web Application