# Docker and Containers

## What are containers 
- lightweight portable units for running applications - bond an application with all its dependencies
- include the code, runtime, libraries, dependencies
- isolated so runs the same on any environment
- can be easily moved between environments
- ensures applications run consistently across different environments
- provides isolation and improves resource efficiency
- work just like real shipping containers
- Container Architecture: 
                                Docker Container
                                 Docker Engine
                              Host Operating System
                                Infrastructure

- Infrastructure - physical or virtual hardware where everything runs
- Host Operating System - OS of infrastrcutre
- Docker Engine - provides the environment to build and run
- Docker Container - holds app and all its dependencies eg bins/libs. Multiple containers will share the same docker engine and host OS, but dont share the env within the container itself

## Benefits of Containers
- Isolation - own environemnts for each application, preventing conflicts/crashes between different version of apps
- Provide consistent running of application, ensuring smooth operation regardless of where its deployed
- share host OS's for efficiency

## Docker
- Open platform for developing, shipping and running applications in containers

### Docker components
- Docker Engine: responsible for creating and running container based on docker file and images instrcutions
- Docker Hub: a cloud service for sharing applications and automating workflows
- Docker compose - a tool that runs multi container docker applications


## Images and containers
- Images (recipe) - templates for creating containers, immutable (unchangeable), created used docker files (series of instructions)
- Containers (dish) - running instances of an images

## Importance in modern development
- Simplified deployment
- Improved efficiency 
- Enhanced collaboration

## VMs vs Containers

### VMs
- VMs allow multiple OS's to run on a single physical machine
- Run on hypervisor instead of a docker engine (heavy weighted) - runs VMs by allocating resources like CPU, memory and storage
- Slower start up time
- Consume more resources
- Stronger isolation - eavh VM has its own kernel system
- Less portable
- VM architecture: 
                App
          Dependencies/packages
              GUEST OS
            Hypervisor
              Host OS
            Infrastructure


### Containers 
- Start within seconds 
- Resource efficient
- Process Level Isolation
- High portability
- Architecture above

## The Dockerfile
- A text file containing a series of instructions on how to build a docker image
- Each instruction creates the layer of an image
- Allow for repeatable builds, meaing you can recreate exact same env everytime
- Structure: 
                FROM
                RUN
                COPY
          WORKDIR / EXPOSE
                CMD

- FROM: specifies the base image to use for the Docker image eg python / js/ node
- RUN: executes commands in the container
- COPY: copies files from the host machine into container
- WORKDIR: sets the working directory for subsequent instructions
- CMD: specifies the command to run when the container starts
- 

