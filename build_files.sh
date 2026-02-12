#!/bin/bash

echo "Building Project..."

# 1. Garante que o pip está instalado
python3 -m ensurepip --default-pip

# 2. Instala as dependências
python3 -m pip install -r requirements.txt

# 3. Coleta os estáticos
echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear
