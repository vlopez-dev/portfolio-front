#!/bin/sh
python manage.py migrate --run-syncdb
python manage.py collectstatic --no-input

gunicorn portafolio.wsgi:application --bind 0.0.0.0:8002

