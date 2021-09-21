from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json

from .models import ChatMessage
from django.contrib.auth.models import User
from channels.db import database_sync_to_async



class ChatroomConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def createMessage(self, sender, message):
        chatMessage = ChatMessage.objects.create(user=User.objects.get(username= sender), message=message)
        chatMessage.save()
    
    # connect to websocket 
    async def connect(self):
        self.room_group_name = 'public_chat'
        
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()
    
    # disconnect from websocket 
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = self.scope['user'].username

        await self.createMessage(sender, message)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
