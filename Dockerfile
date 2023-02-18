FROM --platform=linux/amd64 python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /opt/code

RUN pip install --no-cache-dir psycopg2 poetry==1.1.12

RUN poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install
