import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .tasks import TASKS

class TaskConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.GROUP_NAME = "task-group"
    
    async def connect(self):
        
        await self.channel_layer.group_add(self.GROUP_NAME, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.GROUP_NAME, self.channel_name)


    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        TASKS[data['task_name']].delay(self.GROUP_NAME, *data['args'], **data['kwargs'])
        
        await self.send(text_data=json.dumps({
            "message": f"Task {data['task_name']} started",
        }))

    async def task_complete(self, event):
        await self.send(json.dumps({
            "message": "Task Complete"
        }))