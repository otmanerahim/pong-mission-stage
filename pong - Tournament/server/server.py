# WS server example

import asyncio
import websockets
import MessageType as mp


async def handle_event(websocket, messageType):
    if(messageType == mp.VIEW_CLASSEMENT):
        await websocket.send("classement actuel : ")
    elif (messageType == mp.VIEW_GAMES):
        await websocket.send("parties en cours : ")
    elif(messageType == mp.VIEW_WINNER):
        await websocket.send("Le winner c'est moi !")


async def server(websocket, path):
    message = await websocket.recv()

    await handle_event(websocket, message)


start_server = websockets.serve(server, "localhost", 8600)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
