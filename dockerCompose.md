# Docker Compose

- Tool that offers a powerful and efficient way to manage and run multiple container docker applications 
- Acts as an organiser for all containers (web server, database, caching service)
- YML file acts as the blueprint that describes each container, specifying details like image, port

## Importance of Docker Compose 
- Makes development and testing easier by quickly allowing you to spin up the exact environements needed with all the necessary services 
- Ensures consistency across different environments / devices by ensuring the same CI/CD pipeline uses the same setup
- Enhances teamwork due to shared environments
- Overall streams workflow, reduces errors, better collaboration

## Creating a docker compose .yml 
- 'touch docker-compose.yml' -> creates the docker compose file in directory
- Add contents to docker compose file (see docker-compose.yml)
- 'docker-compose up -d' -> builds all defined services listed in docker yml file in one go (in background)

## Other commands 
- 'docker compose down' -> stops containers
- 'docker-compose logs' -> to see errors