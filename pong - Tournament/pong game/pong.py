from Ball import Ball
from CollisionManager import CollisionManager
from Paddle import Paddle
from PlayerScore import PlayerScore
import numpy as np
import pygame
from ReactionTime import ReactionTime
from BallDirection import BallDirection
from ServerController import ServerController
import MessageType as mt
import asyncio
# ---------
# CONSTANTS
# ---------

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH, HEIGHT = 900, 500
PADDLE_OFFSET = 5
PADDLE_WIDTH = 120
NB_ROUND = 3
NB_POINT = 5
SPEED_BALL = 5
SPEED_PADDLE = 5
round_game = 0
namePlayer1 = ""
namePlayer2 = ""
print("Write the name of first player (left) : ")
namePlayer1 = input()
print("Write the name of second player (right) : ")
namePlayer2 = input()
print("PRESS P TO START THE GAME")


# SCREEN
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PONG')

# ---------
# FUNCTIONS
# ---------


def draw_board():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)


def restart():
    draw_board()
    player1.restart()
    player2.restart()
    ball.restart_pos()
    paddle1.restart_pos()
    paddle2.restart_pos()


def handle_round_and_game_points(player1, player2):
    global round_game
    global playing
    if(int(player1.points) == NB_POINT or int(player2.points) == NB_POINT and round_game < NB_ROUND-1):
        print("Round ", round_game+1, " finished ! ")
        round_game += 1
        draw_board()
        player1.restart()
        player2.restart()
        ball.restart_pos()
        paddle1.restart_pos()
        paddle2.restart_pos()
        ball.start()
    elif(round_game == NB_ROUND):
        playing = False
        round_game = 0
        print("The winner is ", winner(player1, player2))
        restart()
    else:
        ball.start()


def winner(player1, player2):
    if(player1.points > player2.points):
        player1.wonGames += 1
        send_server_message_game(mt.PLAYER_WON, player1.name)
        return player1.name
    else:
        player2.wonGames += 1
        send_server_message_game(mt.PLAYER_WON, player2.name)
        return player2.name


def send_server_message_game(message_type, message):
    global server_controller
    asyncio.get_event_loop().run_until_complete(
        server_controller.send_message_game(message_type, message))


draw_board()

# -------
# OBJECTS
# -------
paddle1 = Paddle(screen, WHITE, 15, HEIGHT//2 -
                 60, PADDLE_OFFSET, SPEED_PADDLE, PADDLE_WIDTH)
paddle2 = Paddle(screen, WHITE, WIDTH - 20 - 15,
                 HEIGHT//2 - 60, PADDLE_OFFSET, SPEED_PADDLE, PADDLE_WIDTH)
ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2, SPEED_BALL, 12)
collision = CollisionManager()
player1 = PlayerScore(screen, '0', namePlayer1, WIDTH//4,  15)
player2 = PlayerScore(screen, '0', namePlayer2, WIDTH -
                      WIDTH//4,  15)
ball_direction = BallDirection(screen, ball)
reaction_time = ReactionTime(200)
server_controller = ServerController()
send_server_message_game(mt.CREATE_PLAYER, namePlayer1)
send_server_message_game(mt.CREATE_PLAYER, namePlayer2)


# ---------
# VARIABLES
# ---------
playing = False

# --------
# MAINLOOP
# --------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not playing and namePlayer1 != "" and namePlayer2 != "":
                ball.start()
                playing = True

            if event.key == pygame.K_r and playing and namePlayer1 != "" and namePlayer2 != "":
                restart()
                playing = False

            if event.key == pygame.K_a:
                paddle1.state = 'up'

            if event.key == pygame.K_z:
                paddle1.state = 'down'

            if event.key == pygame.K_RIGHT:
                paddle2.state = 'up'

            if event.key == pygame.K_LEFT:
                paddle2.state = 'down'

        if event.type == pygame.KEYUP:
            paddle1.state = 'stopped'
            paddle2.state = 'stopped'

    if playing:
        draw_board()

        # ball
        ball.move()
        ball.draw()
        ball_direction.predict_next_coordinate()
        ball_direction.draw()

        # AI 1
        paddle1.advanced_ia(ball_direction, reaction_time.paddle_can_react())
        paddle1.draw()

        # AI 2
        paddle2.advanced_ia(ball_direction, reaction_time.paddle_can_react())
        paddle2.draw()

        # wall collision
        if collision.between_ball_and_walls(ball):
            ball.wall_collision()

        if collision.between_paddle_and_walls_top(paddle1):
            paddle1.wall_collision_top()

        if collision.between_paddle_and_walls_top(paddle2):
            paddle2.wall_collision_top()

        if collision.between_paddle_and_walls_bottom(paddle1):
            paddle1.wall_collision_bottom()

        if collision.between_paddle_and_walls_bottom(paddle2):
            paddle2.wall_collision_bottom()

        # paddle1 collision
        if collision.between_ball_and_paddle1(ball, paddle1):
            ball.paddle_collision_left(paddle1)
            reaction_time.register_tick()
            paddle1.restart_random_attack()

        # paddle2 collision
        if collision.between_ball_and_paddle2(ball, paddle2):
            ball.paddle_collision_right(paddle2)
            reaction_time.register_tick()
            paddle2.restart_random_attack()

        # GOAL OF PLAYER 1 !
        if collision.between_ball_and_goal2(ball):
            draw_board()
            print(player1.name, "scored !")
            player1.increase()
            ball.restart_pos()
            paddle1.restart_pos()
            paddle2.restart_pos()
            handle_round_and_game_points(player1, player2)

        # GOAL OF PLAYER 2!
        if collision.between_ball_and_goal1(ball):
            draw_board()
            print(player2.name, "scored !")
            player2.increase()
            ball.restart_pos()
            paddle1.restart_pos()
            paddle2.restart_pos()
            handle_round_and_game_points(player1, player2)

    player1.show()
    player2.show()

    pygame.display.update()
