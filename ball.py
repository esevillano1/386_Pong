import pygame
from pygame.sprite import Sprite
from random import seed, random


class Ball(Sprite):
    def __init__(self, settings):
        # Initialize the location of the ball

        super().__init__()

        self.settings = settings
        self.radius = self.settings.radius
        self.x = self.settings.horizontalPosition
        self.y = self.settings.screen_height/2
        self.location = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def update(self):
        if self.location.x > 0:
            self.location.x -= self.settings.ball_speed
