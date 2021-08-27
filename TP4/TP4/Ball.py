import pygame
import numpy as np
import random
import math
WIDTH, HEIGHT = 900, 500


class Ball:
    def __init__(self, screen, color, posX, posY, speed,radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.position = np.array((int(posX), int(posY)), dtype=float)
        self.dx = 0
        self.dy = 0
        self.speed = speed
        self.radius = radius
        self.draw()

    def map(self, n, start1, stop1, start2, stop2):
        return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

    def draw(self):
        pygame.draw.circle(self.screen, self.color,
                           (self.posX, self.posY), self.radius)

    def paddle_collision_left(self, paddle1):
        diff = (self.posY) - (paddle1.posY - paddle1.height/2)
        angle = self.map(diff, 0, paddle1.height,
                         -np.radians(45), np.radians(45))
        self.dx = self.speed * np.cos(angle)
        self.dy = self.speed * np.sin(angle)
        self.posX = paddle1.posX + paddle1.width/2 + self.radius

    def paddle_collision_right(self, paddle2):
        diff = (self.posY ) - (paddle2.posY - paddle2.height/2)
        angle = self.map(diff, 0, paddle2.height,
                         np.radians(225), np.radians(135))
        self.dx = self.speed * np.cos(angle)
        self.dy = self.speed * np.sin(angle)
        self.posX = paddle2.posX - paddle2.width/2 - self.radius 

    def start(self):
        angle = np.random.uniform(-np.pi / 4, np.pi / 4)
        self.dx = self.speed * np.cos(angle)
        self.dy = self.speed * np.sin(angle)

    def move(self):
        self.posX += self.dx
        self.posY += self.dy
        self.position = np.array((int(self.posX), int(self.posY)), dtype=float)

    def wall_collision(self):
        self.dy = -self.dy


    def get_dx(self):
        return self.dx

    def get_dy(self):
        return self.dy

    def x_middle(self):
        return self.posX

    def y_middle(self):
        return self.posY

    def restart_pos(self):
        self.posX = WIDTH//2
        self.posY = HEIGHT//2
        self.dx = 0
        self.dy = 0
        self.draw()
