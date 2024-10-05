'''import json
from channels.generic.websocket import WebsocketConsumer

class ProductionConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        # You can extract and process the received data here, e.g. save to the DB
        self.send(text_data=json.dumps({
            'message': 'Data received'
        }))'''


# production/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ProductionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()  # Accept the WebSocket connection

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        print("Received data:", data)

        # Here you can process the data and save it to the DB or do something else

        # Send data back to WebSocket (echo for now)
        await self.send(text_data=json.dumps({
            'message': 'Data received',
            'data': data
        }))
