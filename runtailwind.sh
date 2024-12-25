
#!/bin/sh

current_dir="$(dirname "$(readlink -f "$0")")"

source "$current_dir/.venv/Scripts/activate"

python manage.py tailwind install
python manage.py tailwind start