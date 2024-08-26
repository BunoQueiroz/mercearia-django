#!/bin/bash
# Coleta de arquivos estáticos
python manage.py collectstatic --noinput

# Criação de um arquivo de servidor para o Serverless Functions
echo 'from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()' > server.py
