# syntax=docker/dockerfile:1

FROM python:3.10
# make root directory in our image
RUN mkdir /app
# define working directory
WORKDIR /app
# copy local build into root image
COPY . /app
# install dependencies
RUN pip install --upgrade pip
RUN pip install -e .
# expose port 5000
EXPOSE 5000
# run when users starts the container
CMD ["python", "startup.py"]