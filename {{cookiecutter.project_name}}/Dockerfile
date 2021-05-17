FROM python:3.8

ENV PYTHONUNBUFFERED=1

COPY poetry.lock pyproject.toml /
RUN pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev --no-root

WORKDIR /app
COPY app docker-entrypoint.sh ./

CMD ["./docker-entrypoint.sh"]