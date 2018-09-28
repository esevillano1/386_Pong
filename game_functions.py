import pygame
from pygame.sprite import Group
import sys
from time import sleep

from ball import Ball
from paddle import Paddle


def create_paddles(settings, screen, player_paddles, ai_paddles):
    # Create the player paddles
    playerLeftPaddle = Paddle(settings, screen, "left", "player")
    playerTopPaddle = Paddle(settings, screen, "top", "player")
    playerBottomPaddle = Paddle(settings, screen, "bottom", "player")

    # Create the three ai paddles
    aiRightPaddle = Paddle(settings, screen, "right", "ai")
    aiTopPaddle = Paddle(settings, screen, "top", "ai")
    aiBottomPaddle = Paddle(settings, screen, "bottom", "ai")

    # Add the player paddles to the sprite Group
    player_paddles.add(playerLeftPaddle)
    player_paddles.add(playerTopPaddle)
    player_paddles.add(playerBottomPaddle)

    # Add the ai paddles to their own sprite Group
    ai_paddles.add(aiRightPaddle)
    ai_paddles.add(aiTopPaddle)
    ai_paddles.add(aiBottomPaddle)


def create_ball():
    print("Hello")


def check_keydown_events(event, paddles):
    keys = pygame.key.get_pressed()
    for paddle in paddles:
        if keys[pygame.K_UP] and paddle.wall == "left" and paddle.user == "player":
            paddle.moving_up = True
        elif keys[pygame.K_DOWN] and paddle.wall == "left" and paddle.user == "player":
            paddle.moving_down = True
        elif keys[pygame.K_LEFT] and not keys[pygame.K_LSHIFT] and paddle.wall == "top" and paddle.user == "player":
            paddle.moving_left = True
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LSHIFT] and paddle.wall == "top" and paddle.user == "player":
            paddle.moving_right = True
        # https://stackoverflow.com/questions/12556535/press-multiple-keys-at-once-to-get-my-character-to-move-diagonally
        # Used in understanding how to incorporate left shift in game
        elif keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT] and paddle.wall == "bottom" and paddle.user == "player":
            paddle.moving_left = True
        elif keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT] and paddle.wall == "bottom" and paddle.user == "player":
            paddle.moving_right = True
        elif keys[pygame.K_q]:
            sys.exit()


def check_keyup_events(event, paddles):
    for paddle in paddles:
        if event.key == pygame.K_LEFT:
            paddle.moving_left = False
        elif event.key == pygame.K_RIGHT:
            paddle.moving_right = False
        elif event.key == pygame.K_UP:
            paddle.moving_up = False
        elif event.key == pygame.K_DOWN:
            paddle.moving_down = False


def check_events(settings, screen, paddles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddles)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddles)


def check_play_button():
    print("Hello")


def update_screen():
    print("Hello")


def check_ball_paddle_collisions():
    print("Hello")


def ball_hit():
    print("Hello")