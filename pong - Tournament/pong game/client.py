# WS client example

import asyncio
import websockets
from Message import Message
import MessageType as mt
import json


async def visualize_games(websocket, number):

    if(number == 1):
        msg = {"message_type": mt.VIEW_CLASSEMENT, "message": ""}
        msg_to_send = json.dumps(msg)
        await websocket.send(msg_to_send)
    elif(number == 2):
        msg = {"message_type": mt.VIEW_WINNER, "message": ""}
        msg_to_send = json.dumps(msg)
        await websocket.send(msg_to_send)


async def hello():
    uri = "ws://127.0.0.1:8600"
    async with websockets.connect(uri) as websocket:
        number = input(
            "Selectionner : \n " "1 > Voir le classement actuel  \n Your choice :")

        await visualize_games(websocket, int(number))

        message = await websocket.recv()
        print(f"> {message}")

asyncio.get_event_loop().run_until_complete(hello())
