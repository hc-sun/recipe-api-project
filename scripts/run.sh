#!/bin/sh

set -e

python manage.py wait_db
python manage.py collectstatic --noinput
python manage.py migrate
uwsgi --socket :7000 --workers 4 --master --enable-threads --module app.wsgi
