FROM python:3.9.6

VOLUME /app
WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ENV FLASK_APP app
ENV FLASK_ENV development
ENV FLASK_DEBUG 1

ENTRYPOINT flask run --host=0.0.0.0 --port=80
