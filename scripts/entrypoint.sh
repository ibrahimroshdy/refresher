#!/bin/bash

pyfiglet REFRESHER

echo "Deleting the existing sqllite db..."
rm db.sqlite3

echo "Running makemigrations and migrate..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Loading Fixtures..."
python3 manage.py loaddata django_celery_fixtures

echo "Creating Superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); print('Admin User Exists....') if User.objects.filter(username='admin').exists() else User.objects.create_superuser('admin', 'test@test.com', 'admin') " | python3 manage.py shell

echo "Collecting static.."
echo "yes" | python3 manage.py collectstatic

gunicorn --bind 0.0.0.0:8000 refresher_config.wsgi
