#!/bin/bash

set -e

dockerize -wait tcp://{{cookiecutter.project_name}}-database:5432
gunicorn --bind 0.0.0.0:8000 --workers 2 settings.wsgi:application
