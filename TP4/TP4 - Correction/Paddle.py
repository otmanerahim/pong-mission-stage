
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
        self.random1=np.random.randint(0, self.height/2)
        self.random2=np.random.randint(self.height/2, self.height)
        self.random_position_attack = self.get_random_position_attack()
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.posX,
                         self.posY, self.width, self.height))
    
    
    def get_random_position_attack(self):
        self.random = random.choice([self.random1, self.random2])
        randomOperator = random.choice([True, False])
        
        if(randomOperator==True):
            return self.random1
        return (self.random2)

    def easy_ia(self,ball,can_react):
        if( ball.posY > self.posY+ self.random1 and can_react):
            self.posY += self.dy
        elif( ball.posY < self.posY + self.random2 and can_react):
            self.posY -= self.dy

    def advanced_ia(self,ball,can_react):
        if( ball.get_ball_prediction_y() > self.posY+ self.random1 and can_react):
            self.posY += self.dy
        elif( ball.get_ball_prediction_y() < self.posY + self.random2 and can_react):
            self.posY -= self.dy

    def wall_collision_top(self):
        self.posY += self.dy

    def wall_collision_bottom(self):
        self.posY -= self.dy

    def move_byself(self):
        # moving up
        if self.state == 'up':
            self.posY -= self.dy

        # moving down
        elif self.state == 'down':
            self.posY += self.dy

    
    def restart_random_attack(self):
        self.random1=np.random.randint(0, self.height/2)
        self.random2=np.random.randint(self.height/2, self.height)
        self.random_position_attack = self.get_random_position_attack()

    def restart_pos(self):
        self.posY = HEIGHT//2 - self.height//2
        self.state = 'stopped'
        self.hit_ball = True
        self.draw()
