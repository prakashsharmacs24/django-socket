import asyncio
from uuid import uuid4

from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ItemsConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        while 1:
            await self.send_json(str(uuid4().int >> 64))
            await asyncio.sleep(3)
