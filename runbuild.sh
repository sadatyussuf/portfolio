#!/usr/bin/env bash

set -o errexit  # exit on error
git pull
pip install -r requirements.txt
# cd apps/theme/static_src
# npm install
# # npm run build:clean
# # npm run build:tailwind
# cd ../../..

# python manage.py tailwind build

python manage.py collectstatic --no-input  -i portal

# python manage.py makemigrations
# python manage.py migrate

sudo nginx -t
sudo systemctl restart nginx
sudo systemctl restart adamafrique

