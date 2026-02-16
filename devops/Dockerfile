FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY pyproject.toml poetry.lock /app/

WORKDIR /app

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-root

COPY src/ .
