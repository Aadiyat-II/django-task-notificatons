import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .tasks import long_running_add

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):

        long_running_add.delay(3, 3)
        await self.send(text_data="Hello world!")