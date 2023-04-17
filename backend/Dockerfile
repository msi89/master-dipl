FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

RUN apt-get update && apt-get -y upgrade && \
    apt-get install -y curl git cmake ffmpeg libsm6 libxext6

WORKDIR /app

COPY ./ /app
RUN python -m venv .virtualenv && source .virtualenv/bin/activate

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

ENV PORT=8000

CMD [ "unicorn", "main:app", "--debug" ]