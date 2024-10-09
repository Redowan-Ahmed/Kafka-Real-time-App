#!/bin/bash
# docker-entrypoint.sh
# navigate the directory
cd /KafkaDjango/

# Run the collect static
python3 manage.py collectstatic --noinput

# Start the Gunicorn server
gunicorn config_kafka_realtime.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120