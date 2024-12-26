#!/bin/sh

# current_dir="$(dirname "$(readlink -f "$0")")"

# source "$current_dir/.venv/Scripts/activate"

python manage.py makemigrations && python manage.py migrate
python manage.py runserver