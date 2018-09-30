import pygame
# from pygame.locals import *

# import time
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ball import Ball
from button import Button
import game_functions as gf
from menu import Menu


def run_game():
    # Initialize the game and create a screen object
    pygame.init()

    # Initialize the Settings for the game
    pong_settings = Settings()

    # Create the screen and set the caption
    screen = pygame.display.set_mode((pong_settings.screen_width, pong_settings.screen_height))
    pygame.display.set_caption("Pong")

    # Make the Play Game button.
    play_button = Button(pong_settings, screen, "Play Game", pong_settings.screen_width/4, pong_settings.screen_height/2)

    # Create an instance of the startup menu.
    menu = Menu(pong_settings, screen)

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(pong_settings)
    sb = Scoreboard(pong_settings, screen, stats)

    # # Make the ball and instantiate groups of paddles
    ball = Ball(pong_settings)
    paddles = Group()
    ai_paddles = Group()

    # Create each set of paddles
    gf.create_paddles(pong_settings, screen, paddles, ai_paddles)

    # Activate the left shift key
    pygame.key.set_mods(pygame.KMOD_LSHIFT)

    while True:
        gf.check_events(pong_settings, screen, stats, sb, menu, play_button, ball, paddles)
        if stats.game_active:
            gf.increase_point(pong_settings, stats, sb, ball)
            gf.win_condition(pong_settings, stats, menu)
            gf.update_screen(pong_settings, screen, stats, sb, ball, paddles, ai_paddles)


if __name__ == "__main__":
    run_game()
