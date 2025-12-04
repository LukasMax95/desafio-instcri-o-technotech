#!/bin/bash
# Script: start.sh
# Must have requirements.txt in the root folder
# =======================================================
python3 -m venv workvenv
source workvenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
# =======================================================
# Django Project and App Creation
# =======================================================
mkdir django
cd django
django-admin startproject config .
python3 manage.py startapp api
# =======================================================