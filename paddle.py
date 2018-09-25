import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):
    def __init__(self, settings, wall):
        """Initialize the paddles and set their starting position."""

        super().__init__()

        if wall == "left":
            self.location = pygame.Rect(settings.paddleOffset, settings.verticalPosition, settings.lineThickness, settings.paddleSize)
        elif wall == "right":
            self.location = pygame.Rect(settings.screen_width - settings.paddleOffset - settings.lineThickness, settings.verticalPosition, settings.lineThickness, settings.paddleSize)
        elif wall == "top":
            self.location = pygame.Rect(settings.horizontalPosition, settings.paddleOffset, settings.paddleSize, settings.lineThickness)
        elif wall == "bottom":
            self.location = pygame.Rect(settings.horizontalPosition, settings.screen_height - settings.paddleOffset - settings.lineThickness, settings.paddleSize, settings.lineThickness)

        # Movement flags
        self.moving_left = False
        self.moving_right = False
        self.moving_top = False
        self.moving_down = False

    def update(self):
        """Update the paddle's position based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.paddle_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.paddle_speed_factor
        if self.moving_down and self.rect.down < self.screen_rect.down:
            self.center += self.settings.paddle_speed_factor
        if self.moving_up and self.rect.up > 0:
            self.center -= self.settings.paddle_speed_factor