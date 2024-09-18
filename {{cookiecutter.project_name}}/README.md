# {{cookiecutter.project_name}}


## How to start project
* Install [Python](https://www.python.org/downloads/).
{%- if cookiecutter.package_manager == 'Poetry' %}
* Install [poetry](https://python-poetry.org).
{%- if cookiecutter.package_manager == 'uv' %}
* Install [uv](https://docs.astral.sh/uv/getting-started/installation/).
* Install [Docker](https://docs.docker.com/engine/install/)
* Install [docker-compose](https://docs.docker.com/compose/install/)
{%- if cookiecutter.package_manager == 'Poetry' %}
* Run command `poetry install && poetry shell`
{%- if cookiecutter.package_manager == 'uv' %}
* Run command `uv venv .venv && uv install -r pyproject.toml`
* Run command `make install-pre-commit`
* Run command `make up`
* Run command `make migrate`
* Run command `make createsuperuser`


## How to deploy

## F.A.Q.
