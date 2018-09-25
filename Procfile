web: gunicorn config.wsgi:application
worker: celery worker --app=planfood.taskapp --loglevel=info
