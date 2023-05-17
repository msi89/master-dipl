FROM python:3.10

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y curl git make cmake ffmpeg libsm6 libxext6
    
WORKDIR /app


COPY ./ /app

RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

ENV PORT=8000

CMD [ "uvicorn", "main:app", "--host",  "0.0.0.0"]