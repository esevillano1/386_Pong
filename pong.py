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

    leftPaddle = pygame.Rect(pong_settings.paddleOffset, pong_settings.verticalPosition, pong_settings.lineThickness, pong_settings.paddleSize)
    rightPaddle = pygame.Rect(pong_settings.screen_width - pong_settings.paddleOffset - pong_settings.lineThickness, pong_settings.verticalPosition, pong_settings.lineThickness, pong_settings.paddleSize)
    topPaddle = pygame.Rect(pong_settings.horizontalPosition, pong_settings.paddleOffset, pong_settings.paddleSize, pong_settings.lineThickness)
    bottomPaddle = pygame.Rect(pong_settings.horizontalPosition, pong_settings.screen_height - pong_settings.paddleOffset - pong_settings.lineThickness, pong_settings.paddleSize, pong_settings.lineThickness)

    while True:
        pygame.draw.rect(screen, pong_settings.white, leftPaddle)
        pygame.draw.rect(screen, pong_settings.white, rightPaddle)
        pygame.draw.rect(screen, pong_settings.white, topPaddle)
        pygame.draw.rect(screen, pong_settings.white, bottomPaddle)

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