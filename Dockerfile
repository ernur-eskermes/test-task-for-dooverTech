FROM python:3.9.6-alpine as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev curl \
    && apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers \
    && apk add --no-cache jpeg-dev zlib-dev

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY . .

COPY ./pyproject.toml ./poetry.lock* /usr/src/app/
RUN poetry export -f requirements.txt --dev --output requirements.txt --without-hashes
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt


FROM python:3.9.6-alpine

RUN mkdir -p /home/app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apk update && apk add libpq && apk add --no-cache jpeg-dev zlib-dev
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

COPY . $APP_HOME
