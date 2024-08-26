#!/bin/bash
python3 -m gunicorn setup.wsgi:application --bind 0.0.0.0:$PORT
