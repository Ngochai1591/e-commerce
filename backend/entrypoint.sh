#!/bin/sh
echo "Install Package"
pip install -r requirements.txt

echo "Collect Static"
python manage.py collectstatic --no-input

echo "Migrations"
python manage.py makemigrations && python manage.py migrate

echo "Run Server"
python manage.py runserver 0.0.0.0:8000
exec "$@"