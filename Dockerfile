#dockerfile python workvenv, django restframework, postresql and react/ts + vite
# considerando a arvore de pastas do projeto

FROM python:3.11-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY /test_codes/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django-filter
COPY /django/. /app/
COPY /reacttemplate/. /app/
COPY /test_codes/meu_database.sql /app/meu_database.sql
WORKDIR /app/
EXPOSE 8000
CMD ["sh","-c", "python manage.py migrate && python manage.py runserver", "0.0.0.0:8000"]
# Note: The frontend (React/TS + Vite) part is not included in this Dockerfile. You may want to create a separate Dockerfile for the frontend or use a multi-stage build.