import time
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

@shared_task
def long_running_add(group_name, x, y):
    time.sleep(5)
    print(f"Sum: {x + y}")
    async_to_sync(channel_layer.group_send)(group_name, {"type": "task.complete"})