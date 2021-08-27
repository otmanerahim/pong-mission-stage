
import pygame
import numpy as np
import random
import math
WIDTH, HEIGHT = 900, 500


class Paddle:
    def __init__(self, screen, color, posX, posY, width,speed, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.position = np.array((int(posX), int(posY)), dtype=float)
        self.dy = speed
        self.width = width
        self.height = height
        self.state = 'stopped'
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.posX,
                         self.posY, self.width, self.height))

    def easy_ia(self,ball):
        # Completez l'IA décrite dans l'énoncé

    def move_byself(self):
        # moving up
        if self.state == 'up':
            self.posY -= self.dy

        # moving down
        elif self.state == 'down':
            self.posY += self.dy

    def paddle_hit_ball(self):
        self.hit_ball = True

    def restart_pos(self):
        self.posY = HEIGHT//2 - self.height//2
        self.state = 'stopped'
        self.hit_ball = True
        self.draw()
