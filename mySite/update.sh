#!/bin/bash

git pull
docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
