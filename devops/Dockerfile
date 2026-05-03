FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY pyproject.toml .
RUN pip install --no-cache-dir .

COPY src/ .

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000", "--reload"]
