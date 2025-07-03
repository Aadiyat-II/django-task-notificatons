import os
from celery import Celery

# Set teh defeault Django settings mdoule for the celery program
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

app = Celery("proj")

# Configure celery from Django settings file with its own namespace
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()