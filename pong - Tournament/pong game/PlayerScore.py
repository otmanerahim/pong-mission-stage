import pygame
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WIDTH, HEIGHT = 900, 500


class PlayerScore:
    def __init__(self, screen, points, name, posX, posY):
        self.screen = screen
        self.points = points
        self.name = name
        self.posX = posX
        self.posY = posY
        self.wonGames = 0
        self.font = pygame.font.SysFont("monospace", 80, bold=True)
        self.font_name = pygame.font.SysFont("monospace", 30, bold=True)
        self.label = self.font.render(self.points, 0, WHITE)
        self.label_name = self.font_name.render(self.name, 0, RED)
        self.show()

    def show(self):
        self.screen.blit(
            self.label, (self.posX - self.label.get_rect().width // 2, self.posY-10))
        self.screen.blit(
            self.label_name, (self.posX - self.label.get_rect().width // 2, self.posY+80))

    def increase(self):
        points = int(self.points) + 1
        self.points = str(points)
        self.label = self.font.render(self.points, 0, WHITE)

    def restart(self):
        self.points = '0'
        self.label = self.font.render(self.points, 0, WHITE)
