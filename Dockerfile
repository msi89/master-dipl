FROM python:3.10

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y curl git make cmake ffmpeg libsm6 libxext6

WORKDIR /app

RUN curl -sL https://deb.nodesource.com/setup_18.x | bash - 
RUN apt-get install -y nodejs
