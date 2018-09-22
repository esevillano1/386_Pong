import pygame
from pygame.sprite import Sprite

class Paddle(Sprite):
    def __init__(self, settings, screen):
        """Initialize the paddles and set their starting position."""
        print('Paddle initialized')

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

    def blitme(self):
        """Draw the paddle at its current location."""
        self.screen.blit(self.image, self.rect)