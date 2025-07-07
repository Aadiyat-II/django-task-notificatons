import time
from celery import shared_task

@shared_task
def long_running_add(x, y):
    time.sleep(5)
    print(f"Sum: {x + y}")