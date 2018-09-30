import pygame
from pygame.sprite import Sprite


class Button(Sprite):
    def __init__(self, settings, screen, msg, x, y, text_color=(255, 255, 255), font_size=48):
        """Initialize button attributes."""

        super().__init__()

        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 50, 20
        self.button_color = (0, 0, 0)
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, font_size)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = x
        self.rect.y = y

        self.msg = msg

        # The button message needs to be prepped only once.
        self.prep_msg(self.msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the bottom."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw a blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
