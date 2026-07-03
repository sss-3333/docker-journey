# Docker Networking 
- Managing how containers communicate
- Simplifies the implementation of microservices architecture
- Microservices allow different parts of an application to run as independednt services each in its own container

## Basic Networking Concepts in Docker

### Bridge Network
- Default network mode for containers on the same machine
- Containers connected using tis type of network can communicate via their own IP addresses
- Isolated from host machine network

### Host Network
- Containers use the host machines network directly without any isolation 

### None Network
- Gives a container no network interface
- Used to ensure a container has no network access

## Linking Containers Together
By default, each container is isolated — they can't talk to each other. But in real applications you rarely have just one container. You might have one running your Flask app and another running a database. They need to communicate.
Linking containers just means allowing them to send and receive data between each other

- Creating a custom container allows containers to communicate using container names instead of IP addresses
(see app.py/dockerfile for practical implementation)

- For debugging:
    - 'docker logs [app name]' - lists errors
    - 'dcoker stop [app name]' - stops containers