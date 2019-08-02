import asyncio
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from newspage.models import CheckUpdate

class NewsConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })

        currentuser = self.scope["user"]
        while currentuser:
            UpdateList = await self.returnupdate(currentuser)
            if UpdateList:
                await self.send({
                    "type": "websocket.send",
                    "text": UpdateList
                })
            await asyncio.sleep(10)

    @database_sync_to_async
    def returnupdate(self, currentuser):
        return CheckUpdate(currentuser)