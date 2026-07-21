# 🚀 Dockerized Web Application

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 👨‍💻 Developer

**Himanshu Chhokar**

B.Tech Student  
Shri Vishwakarma Skill University, Palwal

---

# 📌 Project Overview

This project was developed as part of the **CodSoft DevOps Internship – Task 1**.

The application is containerized using Docker and serves a Flask-based portfolio webpage along with a REST API endpoint to verify the application's health.

---

# ✨ Features

- Responsive Portfolio Website
- Dockerized Flask Application
- Gunicorn Web Server
- REST API
- Clean UI
- Docker Compose Support

---

# 🛠️ Tech Stack

- Python
- Flask
- Gunicorn
- Docker
- HTML
- CSS
- JavaScript

---

# 📁 Project Structure

```
task1-dockerized-webapp
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── templates/
├── static/
└── README.md
```

---

# ⚙️ Installation

Clone Repository

```bash
git clone <your-github-repository-link>
```

Move into Project

```bash
cd task1-dockerized-webapp
```

Build Docker Image

```bash
docker build -t docker-webapp .
```

Run Container

```bash
docker run -p 5001:5000 docker-webapp
```

---

# 🌐 Application

Home Page

```
http://localhost:5001
```

API Endpoint

```
GET /api/status
```

Sample Response

```json
{
  "status":"running",
  "message":"Task 1 - Dockerized Web Application is live!"
}
```

---

# 📷 Screenshots

### Home Page

(Add Screenshot Here)

### Docker Running

(Add Screenshot Here)

### API Response

(Add Screenshot Here)

---

# ✅ Verification

```bash
docker ps
```

Expected Output

- Container Running
- Port 5001 Active

---

# 📚 Internship

**CodSoft DevOps Internship**

### Task 1

Dockerized Web Application

---

# 👨‍💻 Author

**Himanshu Chhokar**

GitHub: https://github.com/YourUsername