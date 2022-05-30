#!/bin/bash

pyfiglet REFRESHER

echo "Deleting the existing sqllite db..."
rm db.sqlite3

echo "Running makemigrations and migrate..."
python3 manage.py makemigrations
python3 manage.py migrate

#echo "Running elastic search index..."
#echo "y" | python3 manage.py search_index --rebuild

#echo "Loading Fixtures..."
#python3 manage.py loaddata user_test_data

echo "Creating Superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); print('   USER EXISTS....') if User.objects.filter(username='admin').exists() else User.objects.create_superuser('admin', 'fileyy@email.com', 'admin') " | python3 manage.py shell

echo "Collecting static.."
echo "yes" | python3 manage.py collectstatic

python manage.py runserver 0.0.0.0:8000
