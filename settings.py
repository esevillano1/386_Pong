class Settings():
    """A class to store all settings for Alien invasion."""

    def __init__(self):
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ball Settings.
        self.radius = 3
        self.ball_color = 60, 60, 60

        # How much the paddles and ball are altered after each level.
        self.speedup_scale = 1.3
        self.size_drop_scale = 0.9

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.paddle_speed_factor = 5

    def increase_speed(self):
        """Increase the speed at which the computer's paddle moves."""
        self.paddle_speed_factor *= self.speedup_scale

    def decrease_ball_size(self):
        """Decrease the size of the ball after each level."""
        self.ball_size *= self.size_drop_scale
