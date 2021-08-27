
import pygame
import numpy as np
import random
import math
WIDTH, HEIGHT = 900, 500


class Paddle:
    def __init__(self, screen, color, posX, posY, width, speed, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.position = np.array((int(posX), int(posY)), dtype=float)
        self.origin = np.array(self.position)
        self.velocity = np.array(
            (5, 5), dtype=float)
        self.acceleration = np.zeros(2)
        self.maxforce = 1
        self.maxvelocity = 2
        self.dy = speed
        self.width = width
        self.height = height
        self.state = 'stopped'
        self.random1 = np.random.randint(30, 60)
        self.random2 = np.random.randint(60, 120)
        self.draw()

    def seek(self, ball_pos):
        steer = np.zeros(2)
        # difference to target
        desired = np.array(ball_pos) - self.position
        # normalization
        if np.linalg.norm(desired) > 0:
            desired = desired/np.linalg.norm(desired)
            # magnitude is maxvelocity
            desired = desired*self.maxvelocity
            # calculate steering force
            steer = desired - self.velocity
            # limit force
            if np.linalg.norm(steer) > self.maxforce:
                steer = self.normalizeto(steer, self.maxforce)
        return steer

    def apply_craig_behavior(self, ball_pos, can_react):
        if(can_react):
            self.position = np.array(
                (int(self.posX), int(self.posY)), dtype=float)
            # get new velocity
            self.velocity += self.acceleration

            # Limit velocity to max speed
            if np.linalg.norm(self.velocity) > self.maxvelocity:
                self.velocity = self.normalizeto(
                    self.velocity, self.maxvelocity)
            self.position += self.velocity
            self.acceleration *= 0

            correction_force = (self.seek(ball_pos))
            self.applyForce(correction_force)
            self.move()

    def move(self):
        self.posY = self.position[1] - 0.2

    def applyForce(self, force):
        self.acceleration += force

    def normalizeto(self, vector, max):
        if np.linalg.norm(vector) > 0:
            return (vector/np.linalg.norm(vector)) * max
        else:
            return np.zeros(2)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.posX,
                         self.posY, self.width, self.height))

    def easy_ia(self, ball, can_react):
        if(ball.posY > self.posY + self.random1 and can_react):
            self.posY += self.dy
        elif(ball.posY < self.posY + self.random2 and can_react):
            self.posY -= self.dy

    def advanced_ia(self, ball, can_react):
        if(ball.get_ball_prediction_y() > self.posY + self.random1 and can_react):
            self.posY += self.dy
        elif(ball.get_ball_prediction_y() < self.posY + self.random2 and can_react):
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
        self.random1 = np.random.randint(30, 60)
        self.random2 = np.random.randint(60, 120)

    def restart_pos(self):
        self.posY = HEIGHT//2 - self.height//2
        self.state = 'stopped'
        self.hit_ball = True
        self.draw()
