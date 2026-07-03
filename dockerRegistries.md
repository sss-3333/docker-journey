# Docker Registries

## What is a docker registry / importance
- A system for storing and sharing docker images
- Used as a storage and distribution hub for docker images
- Public registry - open to everyone, has community provides images 
- Private registry - eg ASWER - secure and restricted
- Streamline the deployment process
- Enhance collaboration - everyone on team has access to same resources
- Ensures consistency across teams 
- Workflow:
    - Used to build local image locally
    - Test on a container
    - Push to registry
    - Pull image from registry to deploy in production/staging environment

## Dockerhub
- Public regigstry used for storing, sharing and accessing docker images
- Easily accessible for pulling images to start a project
- Hosts a large collection of community contributed images eg MySQL

## Steps to push a docker image to a registry 
- 'docker build -t [docker hub username]/[docker hub repo name]:[tag ] .' -> build an image and tag with docker hub username
- 'docker push [docker hub username]/[docker hub repo name]:[tag ] -> uploads image to docker under the specified repo name
- 'docker pull [docker hub username]/[docker hub repo name]:[tag ] -> downloads the image to local machine where it can be run as a container

## Steps to push an image to Amazon ECR
- log in to aws
- search ECR
- create private repo and name it 
- copy over command from repos 'view oush commands' tab

## Steps to use docker compose to run a multi-container app using an image pulled from amazon ecr
- replace 'build:' line with:
- image: [ 462774209761.dkr.ecr.us-east-1.amazonaws.com/flask-mysql:latest ]     