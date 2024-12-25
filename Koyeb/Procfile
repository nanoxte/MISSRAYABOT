# (c)TechRewindEditz

web: gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
worker: python src/worker.py
beat: celery -A src.tasks beat --loglevel=info
celery: celery -A src.tasks worker --loglevel=info
