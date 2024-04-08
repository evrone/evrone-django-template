#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
python manage.py collectstatic --no-input --clear
gunicorn --bind 0.0.0.0:8000 --workers 2 settings.wsgi:application --timeout 600 --max-requests 60 --max-requests-jitter 10