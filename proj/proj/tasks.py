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

@shared_task
def long_running_mult(group_name, x, y):
    time.sleep(5)
    print(f"Product: {x * y}")
    async_to_sync(channel_layer.group_send)(group_name, {"type": "task.complete"})

TASKS = {
    "add" : long_running_add,
    "mult" : long_running_mult,
}