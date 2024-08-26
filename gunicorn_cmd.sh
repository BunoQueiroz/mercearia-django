#!/bin/bash
gunicorn setup.wsgi --bind 0.0.0.0:$PORT
