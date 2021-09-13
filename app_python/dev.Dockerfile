FROM python:3.9.6

VOLUME /app
WORKDIR /app
SHELL ["/bin/bash", "-c"]

COPY ./requirements*.txt /tmp/
RUN pip install -r /tmp/requirements.txt -r /tmp/requirements.dev.txt

ENV FLASK_APP app
ENV FLASK_ENV development
ENV FLASK_DEBUG 1

RUN mkdir -p /var/log/sitirits-iu-devops

ENTRYPOINT flask run --host=0.0.0.0 --port=80
