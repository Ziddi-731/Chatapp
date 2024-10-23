from channels.generic.websocket import AsyncWebsocketConsumer
import json
import cv2
import base64
import asyncio
import os
from .getframe import getf
from django.conf import settings
class chatconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name="livestream"
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()
        print("Connected to Client ...")

        self.send("Server is online ...")
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(self.group_name,self.channel_name)
        print("Disonected to Client ...",close_code)
        
    async def receive(self,text_data):
        event_data=json.loads(text_data)
        chat_type= event_data.get('type')
        print(chat_type)
        if chat_type == "chat":
            message = event_data.get("msg")

            # Send the message back to the client
            await self.channel_layer.group_send(self.group_name,{
                'type': 'chat_message',
                'message': message
            })
        
    async def chat_message(self,event):
        msg=event["message"]
        await self.send(text_data=json.dumps({'type':'chat','message':msg}))
    
