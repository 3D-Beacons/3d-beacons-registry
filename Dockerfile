# pull official base image
FROM python:3.8-slim-buster

ADD . /app
WORKDIR /app

RUN pip install -e .
