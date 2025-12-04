#!/bin/bash
# Script: start.sh
# =======================================================
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver
# =======================================================