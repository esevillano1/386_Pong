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

    # # Make the ball and paddles
    # ball = pygame.draw.circle(screen, pong_settings.white, pong_settings.position, pong_settings.radius, pong_settings.width)

    paddles = Group()

    player_paddles = Group()
    ai_paddles = Group()

    gf.create_paddles(pong_settings, screen, player_paddles, ai_paddles)

    paddles.add(player_paddles)
    paddles.add(ai_paddles)

    while True:
        screen.fill(pong_settings.black)
        gf.check_events(pong_settings, screen, paddles)

        pygame.key.set_mods(pygame.KMOD_LSHIFT)

        for paddle in paddles:
            pygame.draw.rect(screen, pong_settings.white, paddle.location)
            paddle.update()

        # ball

        # pygame.draw.line(screen, pong_settings.white, (pong_settings.screen_width/2, 0), (pong_settings.screen_width/2, pong_settings.screen_height))

        pygame.display.flip()


if __name__ == "__main__":
    run_game()
