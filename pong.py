import pygame
# from pygame.locals import *

# import time
from pygame.sprite import Group
from settings import Settings
# from game_stats import GameStats
# from scoreboard import Scoreboard
# from ball import Ball
from paddle import Paddle
# from button import Button
import game_functions as gf

def run_game():
    # Initialize the game and create a screen object
    pygame.init()

    pong_settings = Settings()

    screen = pygame.display.set_mode((pong_settings.screen_width, pong_settings.screen_height))
    pygame.display.set_caption("Pong")

    # # Make the Play Button
    # play_button = Button(pong_settings, screen, "Play game")
    #
    # # Create an instance to store game statistics and create a scoreboard.
    # stats = GameStats(pong_settings)
    # sb = Scoreboard(pong_settings, screen, stats)
    #
    # # Make a ball and the four paddles
    # ball = Ball()

    paddles = Group()
    paddles.add(gf.create_paddles(pong_settings))

    while True:
        for paddle in paddles:
            pygame.draw.rect(screen, pong_settings.white, paddle.location)

        pygame.display.update()

# # Start the main loop for the game
    # while True:
    #     # Watch for keyboard and mouse events.
    #     gf.check_events()
    #
    #     if stats.game_active:
    #         gf.update_paddles()
    #         gf.update_ball()

if __name__ == "__main__":
    run_game()