FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    bash \
    make \
    build-essential \
    && apt-get clean

WORKDIR /model

COPY . . 

RUN pip install --upgrade pip
RUN pip install -r ./config/requirements.txt
