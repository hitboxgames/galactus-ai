# Galactus Mirco Service

Galactus is a micro service which exposes the Jarvis 3D mesh generator model using Flask.  

### Pylint Integration

For developers working on this repository, please be aware that we have integrated `pylint`. Every push to the repository will activate our `pylint` checks. Ensure your code conforms to our coding standards and guidelines. This will help in avoiding any potential build or merge issues.


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
