import pygame


class ReactionTime:
    def __init__(self, reaction_time):
        # Expressed in milliseconds
        self.reaction_time = reaction_time
        self.start_ticks = 0

    def register_tick(self):
        self.start_ticks = pygame.time.get_ticks()

    def paddle_can_react(self):
        millisecondes_elapsed = (
            pygame.time.get_ticks()-self.start_ticks)
        if (millisecondes_elapsed > self.reaction_time):
            return True
            self.start_ticks = 0
        return False
