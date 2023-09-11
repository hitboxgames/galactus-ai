# syntax=docker/dockerfile:1

FROM python:3.11
# make root directory in our image
RUN mkdir /app
# define working directory
WORKDIR /app
# install dependencies
RUN apt-get update && apt-get install -y git
# copy requirements.txt to root image
COPY requirements.txt requirements.txt
# install dependencies
RUN pip install -r requirements.txt
# copy local build into root image
COPY . /app
# install local build
RUN pip install -e .
# expose port 5000
EXPOSE 5000
# run when users starts the container
CMD ["python", "startup.py"]