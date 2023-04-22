#!/bin/bash

# Start the containers
docker-compose -f Docker-compose.prod.yml up -d --build

# Run migrations
docker-compose -f Docker-compose.prod.yml exec web python manage.py makemigrations --noinput
docker-compose -f Docker-compose.prod.yml exec web python manage.py migrate --noinput

# Collect static files
docker-compose -f Docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear