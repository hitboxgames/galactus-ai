# Galactus Micro Service

Galactus is a Flask-based microservice designed to expose the Jarvis 3D mesh generator model. 
The service is hosted on a personal machine and is accessible via `pixelz.duckdns.org:1337`.

## Features

- **Pylint Integration**: Ensures code quality and conformity with coding standards.
- **Access Control**: API key-based authorization for secure access.
- **Various Routes**: Supports generating 3D meshes in GLB and OBJ formats.
- **Health Check Routes**: To ensure the API is running smoothly.
- **Docker Support**: Easy setup and deployment using Docker and `docker-compose`.

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
