from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/", consumers.TaskConsumer.as_asgi()),
]