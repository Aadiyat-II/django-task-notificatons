from .celery import app as celery_app
from .tasks import long_running_add
__all__ = ('celery_app',)
