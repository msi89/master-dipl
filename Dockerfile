FROM python:3.10

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y curl git make cmake ffmpeg libsm6 libxext6

WORKDIR /app


# COPY requirements.txt ./

# RUN pip install -r requirements.txt