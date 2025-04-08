#!/bin/bash

python task_manager/manage.py migrate
python task_manager/manage.py collectstatic --noinput
python task_manager/manage.py runserver 0.0.0.0:8000
