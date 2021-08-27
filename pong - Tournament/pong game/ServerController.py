
import asyncio
import websockets
import json
from Message import Message


class ServerController:
    def __init__(self):
        self.uri = "ws://127.0.0.1:8600"
        self.websocket = ""

    async def send_message_game(self, message_type, message):
        async with websockets.connect(self.uri) as websocket:
            message = {
                "message_type": message_type,
                "message": message
            }
            message_to_send = json.dumps(message)
            await websocket.send(message_to_send)
