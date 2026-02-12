#!/bin/bash

echo "Building Project..."

# 1. Cria um ambiente virtual (venv)
python3.12 -m venv build_venv

# 2. Ativa o ambiente virtual
source build_venv/bin/activate

# 3. Instala as dependências DENTRO do venv
# (Agora o pip vai funcionar sem erro de permissão)
pip install -r requirements.txt

# 4. Coleta os estáticos usando o python do venv
echo "Collect Static..."
python3 manage.py collectstatic --noinput --clear
