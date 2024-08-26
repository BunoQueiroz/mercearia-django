#!/bin/bash
gunicorn setup.wsgi:application --bind 0.0.0.0:$PORT
