class Settings:
    """A class to store all settings for Alien invasion."""

    def __init__(self):
        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Color Options
        self.white = 255, 255, 255
        self.black = 0, 0, 0

        # Paddle Settings.
        self.lineThickness = 5
        self.paddleSize = 150
        self.paddleOffset = 20
        self.verticalPosition = (self.screen_height - self.paddleSize)/2
        self.horizontalPosition = self.screen_width/2

        # Ball Settings.
        self.position = (int(self.screen_width/2), int(self.screen_height/2))
        self.radius = 5
        self.width = 0

        # How much the paddles and ball are altered after each level.
        self.speedup_scale = 1.3
        self.size_drop_scale = 0.9

        # Win conditions
        self.winning_score = 7
        self.winning_games = 3
        self.total_games = 5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.paddle_speed_factor = 5
        self.ball_speed = 1.5

    def increase_speed(self):
        """Increase the speed at which the computer's paddle moves."""
        self.paddle_speed_factor *= self.speedup_scale

    def decrease_ball_size(self):
        """Decrease the size of the ball after each level."""
        self.ball_size *= self.size_drop_scale
