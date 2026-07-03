# Docker Commands

## View Images
### 'docker images'

## Details of image
### 'docker inspect [image ID]'

## Remove images 
### 'docker rmi [image ID]'

## Remove all unused images, containers, networkscollectively
### 'docker system prune

## Remove containers
### 'docker rm [image ID]'

## Building dockerfile
### 'docker build -t hello-flask .'

- docker build -> docker building command 
- -t [name] -> names the container image
- . -> finds dockerfile in that directory


## Running a container 
### 'docker run -d -p 5000:5000 hello-flask'
- -d -> runs the container in detached mode (background)
- -p -> maps port 5002 from machine to 5002 in container
- [name] -> calls container image

### 'docker ps' 
-> info of container including ID

### 'docker stop [ID]' 
-> stops container from running
- Add additional ID if wanting to stop multiple containers

## Creating the network that connects flask app to mysql containers
### 'docker network create [naame of network]'

## To run mysql container and setting root password for authentication
### 'docker run -d --name [db name] --network [custom network name] -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:[version number]'

## To build docker image for flask app and run application
### 'docker build -t [image name]-mysql .'
### -> 'docker run -d --name [name of app] --network [custom network] -p [port number]:[port number] [image name]-mysql'

### 'docker compose down' 
-> stops containers

### 'docker-compose logs' 
-> to see errors

## Making Images Lighter: Multistage Builds
- See Dockerfile for this implementaion