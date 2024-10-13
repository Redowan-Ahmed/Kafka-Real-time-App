import ujson as json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async


class DeliveryLocationUpdate(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'delivery_location_%s' % self.room_name
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print(code)
        return await super().disconnect(code)

    async def receive(self, text_data=None, bytes_data=None):

        if bytes_data:
            decoded_data = bytes_data.decode('utf-8')  # Convert bytes to string

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "send_live_location",
                    "message": bytes_data,  # Forward the decoded byte data
                }
            )

        if text_data:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "send_live_location",
                    "message": text_data,
                }
            )

    async def send_live_location(self, event):
        print('send_live_', event)

        message = event['message']
        if isinstance(message, str):
            # Send as text if it's a string
            await self.send(text_data=json.dumps({"message": message}))
        else:
            # Send as bytes if it's binary
            # Convert string to bytes
            await self.send(bytes_data=message)
