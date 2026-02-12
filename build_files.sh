#!/bin/bash

echo "Building Project..."

# Garante o pip
python3.12 -m ensurepip --default-pip

# Instala dependências
python3.12 -m pip install -r requirements.txt

# Coleta estáticos
echo "Collect Static..."
python3.12 manage.py collectstatic --noinput --clear
