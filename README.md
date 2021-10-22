# Evrone Django Template

![https://evrone.com/?utm_source=evrone-django-template](https://img.shields.io/badge/%2Fevrone-%20%20-blue) ![https://github.com/evrone/evrone-django-template/blob/master/LICENSE](https://img.shields.io/github/license/evrone/evrone-django-template)  


## About
Template for Django projects based on:
- Simplicity
- Purity
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [The Twelve-Factor App](https://12factor.net) 


## Features
- [`poetry`](https://python-poetry.org) modern Python package manager.
- [OpenAPI](https://spec.openapis.org/oas/latest.html) endpoint at `/openapi`
- [`.pre-commit`](https://pre-commit.com) hooks with predefined [`black`]([`poetry`](https://python-poetry.org) modern Python package manager.) and [`isort`](https://github.com/PyCQA/isort) configs.
- [`pytest`](https://docs.pytest.org/en/6.2.x/) with basic setup
- Basic dependencies such `django`, `djangorestframework` etc.
- `docker-compose` infrastructure file with database ([PostgreSQL](https://www.postgresql.org)) and cache ([Redis](https://redis.io)).
- Dockerfile for application deployment
- Settings based on environment variables.
- Health check endpoint at `/health`


## Quick start
1. Install [cookiecutter](https://github.com/cookiecutter/cookiecutter).
2. Run command `cookiecutter git@github.com:evrone/evrone-django-template.git`.
3. Follow instructions.

---

[<img src="https://evrone.com/logo/evrone-sponsored-logo.png" width=231>](https://evrone.com/?utm_source=evrone-django-template)