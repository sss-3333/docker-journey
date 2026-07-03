## Containerising web application

#FROM python:3.8-slim
#WORKDIR /app
#COPY . .
#RUN apt-get update && apt-get install -y \
#    gcc \
#    python3-dev \
#    libmariadb-dev \
#    pkg-config
#RUN pip install flask mysqlclient
#EXPOSE 5000
#CMD ["python", "app.py"]



## Making images lighter by using multistage builds and removing all unncessary build tools

# Stage 1: Build stage
FROM python:3.8-slim AS build
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config
#order of copying directories is changed
COPY . .                          
RUN pip install flask mysqlclient

# Stage 2: Production stage
FROM python:3.8-slim
WORKDIR /app
# only copy necessary directories
COPY --from=build /app /app
EXPOSE 5000
CMD ["python", "app.py"]
