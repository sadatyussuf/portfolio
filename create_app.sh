#!/bin/bash

echo "Enter folder name: "
read folder_name

echo "Enter app name: "
read app_name

# current_dir="$(dirname "$(readlink -f "$0")")"

cd $folder_name

../manage.py startapp $app_name

cd ..

echo "Hurrah, app $app_name! has succefully been created  in apps folder"