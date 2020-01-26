# base image
FROM python:3.7-alpine

# set working directory
WORKDIR /usr/src/app

RUN apk --update add build-base

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
ADD . /usr/src/app

EXPOSE 8000