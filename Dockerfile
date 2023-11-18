# start dockeer with python 3.11
FROM python:3.11.6-slim-bullseye

# setup linux 
ENV PYTHONUNBUFFERED = 1

# install needed libraries 
RUN apt-get update && apt-get -y install libpq-dev gcc

# create project folder 
WORKDIR /app


# copy requirements ---> app
COPY requirements.txt /app/requirements.txt


# install libraries
RUN pip install -r /app/requirements.txt


# copy all files --> app
COPY . /app/