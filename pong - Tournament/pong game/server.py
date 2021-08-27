# WS server example

import asyncio
import websockets
import MessageType as mp
import json
from PlayerTournament import PlayerTournament

list_players = []


def get_classement():
    global list_players
    classement = []
    winner = ""
    indexW = 0
    while(len(list_players) > 1):
        winner = list_players[0]
        for i in range(0, len(list_players)):
            if(list_players[i].points > winner.points):
                winner = list_players[i]
                indexW = i

        classement.append(winner)
        list_players.pop(indexW)

    classement.append(list_players[0])
    return classement


async def handle_event(websocket, message):
    global list_players
    message = json.loads(message)
    if(message["message_type"] == mp.VIEW_CLASSEMENT):
        clsmt = get_classement()
        classement_message = ""
        for i in range(0, len(clsmt)):
            print(clsmt[i].name)
            classement_message += "Player  : {} , Points : {} \n".format(
                clsmt[i].name, clsmt[i].points)
        await websocket.send(classement_message)
    elif(message["message_type"] == mp.VIEW_WINNER):
        winner = list_players[0]
        for player in list_players:
            if(player.points >= winner.points):
                winner = player
        await websocket.send(winner.name)
    elif(message["message_type"] == mp.CREATE_PLAYER):
        print("Ajout du joueur", message["message"])
        list_players.append(PlayerTournament(message["message"]))
    elif(message["message_type"] == mp.PLAYER_WON):
        for player in list_players:
            if(message["message"] == player.name):
                player.points += 1
                player.to_string()


async def server(websocket, path):
    message = await websocket.recv()

    await handle_event(websocket, message)


start_server = websockets.serve(server, "localhost", 8600)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
