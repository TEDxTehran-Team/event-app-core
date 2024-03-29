import os

from celery import Celery
from event_app.components.celery import Config

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_app.settings')

app = Celery('event_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(Config, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()