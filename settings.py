class Settings:

    def __init__(self):
        self.screen_width = LOW_RES.WIDTH
        self.screen_height = LOW_RES.HEIGHT

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        print('Dynamic Settings')

