import pygame.font
from pygame.sprite import Group

from paddle import Paddle

class Scoreboard():
    """A class to report scoring information."""
    def __init__(self, settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score('player1')
        self.prep_score('player2')
        self.prep_high_score()
        self.prep_level()

    def prep_score(self, user):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Align the score in the appropriate location
        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 20
        if user == 'player1':
            self.score_rect.midtop = self.screen_rect.midtop - 10
        elif user == 'player2':
            self.score_rect.midtop = self.screen_rect.midtop + 10

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        """Turn the score into a rendered image."""
        high_score = int(round(self.stats.score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.high_score_rect.top

    def show_score(self):
        """Draw scores and paddles to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # Draw paddles.
        self.paddles.draw(self.screen)

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(stats.level), True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10