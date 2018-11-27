#!/bin/bash

docker-compose build
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
