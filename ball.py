import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, settings):
        # Initialize the location of the ball

        super().__init__()

        self.settings = settings
        self.radius = self.settings.radius
        self.x = self.settings.horizontalPosition
        self.y = self.settings.screen_height/2
        self.location = pygame.Rect(self.x, self.y, self.radius, self.radius)
        self.xdir = 1
        self.ydir = 1

    def update(self):
        self.location.x += (self.settings.ball_speed_x * self.xdir)
        self.location.y += (self.settings.ball_speed_y * self.ydir)
