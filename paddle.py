import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    def __init__(self, settings, screen, wall, user):
        """Initialize the paddles and set their starting position."""

        super().__init__()

        # Attributes to allow the paddle to be distinguished between player an ai
        self.user = user
        self.wall = wall

        # Values used in assigning location of paddle
        self.hor = settings.horizontalPosition
        self.vert = settings.verticalPosition
        self.wide = settings.lineThickness
        self.long = settings.paddleSize
        self.height = settings.screen_height
        self.width = settings.screen_width
        self.offset = settings.paddleOffset

        # Values used when moving the paddles
        self.settings = settings
        self.screen_rect = screen.get_rect()

        # Adjust the location of the paddle based on the position and user
        if self.wall == "left":
            self.location = pygame.Rect(self.offset, self.vert, self.wide, self.long)
        elif self.wall == "right":
            self.location = pygame.Rect(self.width - self.offset - self.wide, self.vert, self.wide, self.long)
        elif self.wall == "top":
            if self.user == "player":
                self.hor -= self.width/4 + self.long/2
                self.location = pygame.Rect(self.hor, self.offset, self.long, self.wide)
            elif self.user == "ai":
                self.hor += self.width/4 - self.long/2
                self.location = pygame.Rect(self.hor, self.offset, self.long, self.wide)
        elif self.wall == "bottom":
            if self.user == "player":
                self.hor -= self.width/4 + self.long/2
                self.location = pygame.Rect(self.hor, self.height - self.offset - self.wide, self.long, self.wide)
            elif self.user == "ai":
                self.hor += self.width/4 - self.long/2
                self.location = pygame.Rect(self.hor, self.height - self.offset - self.wide, self.long, self.wide)

        # Movement flags
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the paddle's position based on the movement flags."""
        if self.moving_right and self.location.x + self.long < self.width/2:
            self.location.x += self.settings.paddle_speed_factor
        if self.moving_left and self.location.x > 0:
            self.location.x -= self.settings.paddle_speed_factor
        if self.moving_down and self.location.y + self.long < self.height:
            self.location.y += self.settings.paddle_speed_factor
        if self.moving_up and self.location.y > 0:
            self.location.y -= self.settings.paddle_speed_factor

    # Use to test the movement of the paddles
    def __str__(self):
        print("wall: " + str(self.wall) + " x: " + str(self.location.centerx) + " y: " + str(self.location.centery) + " screen width: " + str(self.width) + " screen height: " + str(self.height))