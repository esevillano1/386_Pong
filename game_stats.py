class GameStats:
    def __init__(self, settings):
        """Initialize statistics."""
        self.settings = settings
        self.reset_stats()

        # Start Pong in an active state.
        self.game_active = False

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can be changed throughout the game."""
        self.player_score = 0
        self.computer_score = 0
        self.level = 1