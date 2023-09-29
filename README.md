## Backend application
Use `docker-compose.yml` file to run backend, postgres  services. Docker volumes are used to persist data stored in Postgres databases. 

The command to run - `docker compose up --build`. It will build backend Docker image from Dockerfile and pull `postgres:alpine`  Docker image and run services.

To configure backend service and Postgres add `.env` file. Add necessary environment variables before you run `docker compose up` command.

Environment variables to add into `.env` file:
- DATABASE_SECRET_KEY
- DATABASE_HOST
- SECRET_KEY
- DJANGO_SUPERUSER_USERNAME
- DJANGO_SUPERUSER_PASSWORD

Environment variables to add into `.env` file:
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB