# 🐋 Docker Module 

## Overview
This module covers containerisation using Docker — from core concepts to building and deploying multi-container applications.

---

## Concepts Covered

### Containers vs Virtual Machines

### Docker Core Components
- **Dockerfile** 
- **Image** 
- **Container** 
- **Docker Compose** 
- **Registry** 
---

## Projects

### 1. Flask + MySQL (`hello_flask/`)
A simple Flask web application containerised with Docker, connected to a MySQL database.

**Key concepts applied:**
- Writing a Dockerfile using multistage builds to reduce image size
- Running containers on a custom network so Flask and MySQL can communicate
- Using Docker Compose to manage both services with a single command
- Pushing images to Docker Hub and Amazon ECR

**Run locally:**
```bash
docker compose up -d
```
Visit `http://localhost:5000`

---

### 2. Flask + Redis — Velvet Count (`challenge_task/`)
A multi-container application with a styled Flask frontend and Redis as a key-value store to track visit counts.

**Key concepts applied:**
- Redis as a database — using `INCR` to increment a visit counter
- Docker Compose networking — containers communicate by service name
- Environment variables for Redis connection details
- Persistent Redis volumes so data survives container restarts

**Run locally:**
```bash
docker compose up -d
```
Visit `http://localhost:5001` and `/count`

---

## Project Visuals
![Velvet Count Homepage](project-visuals/velvet-count-home.png)
![Velvet Count Counter](project-visuals/velvet-count-counter.png)

## Image Registries

Images were pushed to two registries:

- **Docker Hub** — `sss3333/flask-mysql`
- **Amazon ECR** — `462774209761.dkr.ecr.us-east-1.amazonaws.com/flask-mysql`

### ECR Push Workflow
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ecr-uri>
docker tag flask-mysql:latest <ecr-uri>:latest
docker push <ecr-uri>:latest
```

---

## Key Commands

| Command | Description |
|---|---|
| `docker build -t my-app .` | Build an image |
| `docker run -d -p 5000:5000 my-app` | Run a container |
| `docker compose up -d` | Start all services |
| `docker compose up --build -d` | Rebuild and start |
| `docker compose down` | Stop all services |
| `docker ps` | List running containers |
| `docker images` | List local images |
| `docker logs <container>` | View container logs |

---

## Tools & Technologies
- Docker & Docker Compose
- Python / Flask
- MySQL & Redis
- Amazon ECR
- AWS CLI