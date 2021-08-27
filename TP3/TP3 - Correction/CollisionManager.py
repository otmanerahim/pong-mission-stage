import pygame
import numpy as np
WIDTH, HEIGHT = 900, 500

PADDLE_OFFSET = 5


class CollisionManager:


    def between_paddle_and_walls_bottom(self,paddle):
        if(paddle.posY > HEIGHT - paddle.height):
            return True

        return False

    def between_paddle_and_walls_top(self,paddle): 
        if(paddle.posY < 0 ):
            return True
        return False


    def between_ball_and_paddle1(self, ball, paddle):
        ballX = ball.posX
        ballY = ball.posY
        paddleX = paddle.posX
        paddleY = paddle.posY
        if (ballX < paddleX - paddle.width and ballY < paddleY + paddle.height and ballY > paddleY - paddle.height ):
            if (ballX - ball.radius < paddleX):
                return True
        return False

    def between_ball_and_paddle2(self, ball, paddle):
        ballX = ball.posX
        ballY = ball.posY
        paddleX = paddle.posX
        paddleY = paddle.posY
        if (ballX > paddleX - paddle.width and ballY < paddleY + paddle.height and ballY > paddleY - paddle.height ):
            if (ballX + ball.radius > paddleX):
                return True
            return True
        return False

    def between_ball_and_walls(self, ball):
        ballY = ball.posY

        # top collision
        if ballY - ball.radius <= 0:
            return True

        # bottom collision
        if ballY + ball.radius >= HEIGHT:
            return True

         # no collision
        return False

    def between_ball_and_goal1(self, ball):
        return ball.posX + ball.radius <= 0

    def between_ball_and_goal2(self, ball):
        return ball.posX - ball.radius >= WIDTH 
