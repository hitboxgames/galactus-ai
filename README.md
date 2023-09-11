# Galactus Micro Service

Galactus is a Flask-based microservice designed to expose the Jarvis 3D mesh generator model. 
The service is hosted on a personal machine and is accessible via `pixelz.duckdns.org:1337`.

## Features

- **Pylint Integration**: Ensures code quality and conformity with coding standards.
- **Access Control**: API key-based authorization for secure access.
- **Various Routes**: Supports generating 3D meshes in GLB and OBJ formats.
- **Health Check Routes**: To ensure the API is running smoothly.
- **Docker Support**: Easy setup and deployment using Docker and `docker-compose`.

## API Endpoints

### Public Routes

- `GET /`: Home route that serves as a verification that the API is working. No API key required.

### Protected Routes (API Key Required)

Reach out to Gino Rey to obtain an API key. The API key must be included in the request headers.

- `POST /generate_glb`: Generate a GLB 3D mesh. Requires a JSON object in the format `{"prompt": "a car"}`.
  
- `POST /generate_obj`: Generate an OBJ 3D mesh. Requires a JSON object in the format `{"prompt": "a car"}`.

- `POST /ping`: Verifies the API's latency.
- 
- `GET /health_check`: Verifies that the API is operational.

## Hosting and Networking

We are using port forwarding to expose our local network service to the internet. 
Requests to `pixelz.duckdns.org:1337` are directed to our local machine via port forwarding. 

### How it Works

1. **Local Network Setup**: Our local network is configured to forward incoming traffic on port 1337 to the machine where the Galactus service is hosted.
  
2. **NGINX Container**: On this machine, we have an NGINX container running that listens on port 1337.

3. **Routing**: NGINX is configured as a reverse proxy to route the incoming requests to the Galactus container.

This setup allows us to securely manage and route incoming internet traffic to our local service, making it accessible from the outside world.

## Requirements

* Docker. Please, note that `docker-compose` is needed too and is included in
the Docker Desktop installation. Docker Desktop is available for
[Mac](https://docs.docker.com/desktop/install/mac-install/),
[Windows](https://docs.docker.com/desktop/install/windows-install/) and
[Linux](https://docs.docker.com/desktop/install/linux-install/).

Note that you do not necessarily need to install Docker Desktop. You can also
install [Docker Engine](https://docs.docker.com/engine/install/) and
[docker-compose](https://docs.docker.com/compose/install/). In that case,
please use `docker-compose` instead of `docker compose` in all commands below.

## Running Locally without Docker

Install all requirements, then run the app entry point.
```bash
$ pip install -e .
$ python3 startup.py
```

## Running Locally with Docker

Run the premade docker-compose script.
```bash
$ ./deploy.sh
```
