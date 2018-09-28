import pygame
# from pygame.locals import *

# import time
from pygame.sprite import Group
from settings import Settings
# from game_stats import GameStats
# from scoreboard import Scoreboard
from ball import Ball
# from paddle import Paddle
# from button import Button
import game_functions as gf


def run_game():
    # Initialize the game and create a screen object
    pygame.init()

    # Initialize the Settings for the game
    pong_settings = Settings()

    # Create the screen and set the caption
    screen = pygame.display.set_mode((pong_settings.screen_width, pong_settings.screen_height))
    pygame.display.set_caption("Pong")

    # # Make the ball and instantiate groups of paddles
    ball = Ball(pong_settings)
    paddles = Group()
    player_paddles = Group()
    ai_paddles = Group()

    # Create each set of paddles
    gf.create_paddles(pong_settings, screen, player_paddles, ai_paddles)

    # Add the player and ai paddles to the group of paddles
    paddles.add(player_paddles)
    paddles.add(ai_paddles)

    # Activate the left shift key
    pygame.key.set_mods(pygame.KMOD_LSHIFT)

    while True:
        gf.update_screen(pong_settings, screen, ball, paddles)
        gf.check_events(pong_settings, screen, paddles)


if __name__ == "__main__":
    run_game()
