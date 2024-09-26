FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY /scripts/wait-for-it.sh /wait-for-it.sh
RUN chmod +x wait-for-it.sh

COPY /scripts/start.sh /start.sh
RUN chmod +x /start.sh

COPY /scripts/start-dev.sh /start-dev.sh
RUN chmod +x /start-dev.sh

{%- if cookiecutter.package_manager == 'Poetry' %}

COPY poetry.lock pyproject.toml /
RUN pip install poetry==1.8.2 \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev --no-root
{%- elif cookiecutter.package_manager == 'uv' %}

COPY uv.lock pyproject.toml /
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
  && uv install -r pyproject.toml
{%- endif %}

WORKDIR /app

COPY app ./
