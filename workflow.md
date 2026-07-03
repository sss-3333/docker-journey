# Full Workflow for Setting up an app with Docker

## 1. Write the application
Create app.py (Flask web app)
Test it runs locally first

## 2. Containerise it
Write a Dockerfile with instructions to build the image
Build the image: docker build -t my-app .
Run it locally to test: docker run -p 5000:5000 my-app
Verify it works in the browser at localhost:5000

## 3. Add a database
Choose your database (MySQL, Redis, PostgreSQL etc) and run it as a container: docker run --name redisdb [ dbname ] -p [ port number: port number] [ dbname ]
Connect it to your app container via a shared network — either manually with docker network create or automatically through Docker Compose 
OR SKIP TO STEP 4 AND RUN IT ALTOGETHER

## 4. Simplify with Docker Compose
Write a docker-compose.yml defining both services
Replace all the manual docker run commands with just: docker compose up -d
If changes are made to Docker-compose.yml after running docker compose up, must run: 'docker compose up --build' so image is created again

## 5. Push to a registry
Docker Hub: docker push sss-3333/my-app:latest
ECR: docker push 462774209761.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
ACR (Azure): docker push myregistry.azurecr.io/my-app:latest
