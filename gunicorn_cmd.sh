#!/bin/bash
chmod +x gunicorn_cmd.sh
echo "Estou passando pelo build!"
gunicorn setup.wsgi:application --bind 0.0.0.0:$PORT
