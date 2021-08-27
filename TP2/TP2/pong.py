from Ball import Ball
from CollisionManager import CollisionManager
from Paddle import Paddle
from PlayerScore import PlayerScore
import numpy as np
import pygame
# ---------
# CONSTANTS
# ---------

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SPEED_PADDLE=2
SPEED_BALL=1
WIDTH, HEIGHT = 900, 500
PADDLE_OFFSET = 5
PADDLE_WIDTH = 120


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
    score1.restart()
    score2.restart()
    ball.restart_pos()
    paddle1.restart_pos()
    paddle2.restart_pos()


draw_board()

# -------
# OBJECTS
# -------
paddle1 = Paddle(screen, WHITE, 15, HEIGHT//2 -
                 60, PADDLE_OFFSET, SPEED_PADDLE, PADDLE_WIDTH)
paddle2 = Paddle(screen, WHITE, WIDTH - 20 - 15,
                 HEIGHT//2 - 60, PADDLE_OFFSET, SPEED_PADDLE, PADDLE_WIDTH)
ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2,SPEED_BALL, 12)
collision = CollisionManager()
score1 = PlayerScore(screen, '0', WIDTH//4, 15)
score2 = PlayerScore(screen, '0', WIDTH - WIDTH//4, 15)


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
            if event.key == pygame.K_p and not playing:
                ball.start()
                playing = True

            if event.key == pygame.K_r and playing:
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

       # Player
        paddle1.easy_ia(ball)
        paddle1.draw()

        # AI
        paddle2.easy_ia(ball)
        paddle2.draw()

        # wall collision
        if collision.between_ball_and_walls(ball):
            ball.wall_collision()

        # paddle1 collision
        if collision.between_ball_and_paddle1(ball, paddle1):
            ball.paddle_collision_left(paddle1)
            paddle1.paddle_hit_ball()

        # paddle2 collision
        if collision.between_ball_and_paddle2(ball, paddle2):
            ball.paddle_collision_right(paddle2)
            paddle2.paddle_hit_ball()

        # GOAL OF PLAYER 1 !
        if collision.between_ball_and_goal2(ball):
            draw_board()
            score1.increase()
            ball.restart_pos()
            paddle1.restart_pos()
            paddle2.restart_pos()
            playing = False

        # GOAL OF PLAYER 2!
        if collision.between_ball_and_goal1(ball):
            draw_board()
            score2.increase()
            ball.restart_pos()
            paddle1.restart_pos()
            paddle2.restart_pos()
            playing = False

    score1.show()
    score2.show()

    pygame.display.update()
