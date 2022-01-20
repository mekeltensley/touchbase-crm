python manage.py collectstatic --no-input

python manage.py migrate

waitress-serve --port=80 touchbasecrm.wsgi:application