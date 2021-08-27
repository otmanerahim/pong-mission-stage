# WS client example

import asyncio
import websockets
from Message import Message
import MessageType as mt


async def visualize_games(websocket, number):
    if(number == 1):
        await websocket.send(mt.VIEW_CLASSEMENT)
    elif(number == 2):
        await websocket.send(mt.VIEW_GAMES)
    elif(number == 3):
        await websocket.send(mt.VIEW_WINNER)


async def hello():
    uri = "ws://127.0.0.1:8600"
    async with websockets.connect(uri) as websocket:
        number = input(
            "Selectionner : \n " "1 > Voir le classement actuel \n 2 > Voir le gagnant actuel du tournoi \n 3 > Voir les parties en cours \n Your choice :")

        await visualize_games(websocket, int(number))

        message = await websocket.recv()
        print(f"> {message}")

asyncio.get_event_loop().run_until_complete(hello())
