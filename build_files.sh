#!/bin/bash
echo "Building Project..."
python3.9 -m pip install -r requirements.txt

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
