FROM python:3.9.6

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP app

ENTRYPOINT flask run --host=0.0.0.0 --port=80
