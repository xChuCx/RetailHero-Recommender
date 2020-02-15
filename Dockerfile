# base image
FROM python:3.8.1-slim

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apt-get update \
    && apt-get -y install gcc g++

RUN pip install -r requirements.txt



# add app
ADD . /usr/src/app

EXPOSE 8000