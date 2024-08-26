#!/bin/bash
chmod +x gunicorn_cmd.sh
echo("\nEstou passando pelo build!\n")
gunicorn setup.wsgi:application --bind 0.0.0.0:$PORT
