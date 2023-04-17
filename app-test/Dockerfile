FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10


WORKDIR /app


COPY ./ /app

RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate

RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

ENV PORT=8000

CMD [ "uvicorn", "main:app", "--host",  "0.0.0.0"]