FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

COPY poetry.lock pyproject.toml /
RUN pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev --no-root

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

WORKDIR /app
COPY app docker-entrypoint.sh ./

CMD ["./docker-entrypoint.sh"]