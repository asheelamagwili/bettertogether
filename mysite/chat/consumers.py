# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        #print(self.user)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        # The chat
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # The usernames
        self.user = self.scope['user']
        user = '%s' % self.user

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        print(user)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user
        }))


class BoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
    
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from WebSocket
    async def receive(self, text_data):
        # The command
        text_data_json = json.loads(text_data)
        coordinates = text_data_json['coordinates']

        # The usernames
        self.user = self.scope['user']
        user = '%s' % self.user
        print("CANVAS RECEIVED COORDINATES FROM SOCKET\n")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'coordinates': coordinates,
                'user': user
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        coordinates = event['coordinates']
        user = event['user']
        print("user: ")
        print(user)
        print("coordinates: ")
        print(coordinates)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'coordinates': coordinates,
            'user': user
        }))


# Documentation on Channels Authentication
# https://channels.readthedocs.io/en/latest/topics/authentication.html
