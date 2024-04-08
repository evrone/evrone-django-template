#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py runserver 0.0.0.0:8000