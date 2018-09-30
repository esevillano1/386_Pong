import pygame.font


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font_size = 32
        self.font = pygame.font.SysFont(None, self.font_size)

        # Prepare the initial score images.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        player_rounded_score = int(self.stats.player_score)
        player_score_str = "{:,}".format(player_rounded_score)
        self.player_score_image = self.font.render(player_score_str, True, self.text_color, self.settings.bg_color)

        ai_rounded_score = int(self.stats.ai_score)
        ai_score_str = "{:,}".format(ai_rounded_score)
        self.ai_score_image = self.font.render(ai_score_str, True, self.text_color, self.settings.bg_color)

        # Align the score in the appropriate location
        self.player_score_rect = self.player_score_image.get_rect()
        self.player_score_rect.top = self.settings.screen_height/8

        self.ai_score_rect = self.player_score_image.get_rect()
        self.ai_score_rect.top = self.settings.screen_height / 8

        self.player_score_rect.centerx = self.settings.screen_width/6
        self.ai_score_rect.centerx = self.settings.screen_width/1.3

    def show_score(self):
        """Draw scores and paddles to the screen."""
        self.screen.blit(self.player_score_image, self.player_score_rect)
        self.screen.blit(self.ai_score_image, self.ai_score_rect)
