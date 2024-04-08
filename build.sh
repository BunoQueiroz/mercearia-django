#!/bin/bash

apt-get install postgresql-dev gcc musl-dev

pip install --upgrade pip
# Instalar as dependências Python
pip install -r requirements.txt

# Executar as migrações do banco de dados, se necessário
python manage.py migrate

# Outras tarefas de construção, como compilar assets estáticos
python manage.py collectstatic --no-input
