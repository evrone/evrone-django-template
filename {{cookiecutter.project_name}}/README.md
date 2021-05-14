# {{cookiecutter.project_name}}


## How to start project
* Install [Python](https://www.python.org/downloads/).
* Install [poetry](https://python-poetry.org).
* Install [Docker](https://docs.docker.com/engine/install/)
* Install [docker-compose](https://docs.docker.com/compose/install/)
* Run command `poetry install && poetry shell`
* Run command `pre-commit install`
* Generate secret key at `https://djecrety.ir`
* Create file `.env` at `app/settings` level with following content:
  ```
  SECRET_KEY=<paste-here-secret-key-from-previous-step>
  ```
* Run command `docker-compose up -d`
* Run command `python manage.py migrate`
* Run command `python manage.py runserver`


## How to deploy

## F.A.Q.
