import pygame
from pygame.sprite import Group
import sys
from time import sleep

from ball import Ball
from paddle import Paddle


def create_paddles(settings):
    # Create the Group paddles
    paddles = Group()

    # Create all four paddles
    leftPaddle = Paddle(settings, "left")
    rightPaddle = Paddle(settings, "right")
    topPaddle = Paddle(settings, "top")
    bottomPaddle = Paddle(settings, "bottom")

    # Add the paddles to the sprite Group
    paddles.add(leftPaddle)
    paddles.add(rightPaddle)
    paddles.add(topPaddle)
    paddles.add(bottomPaddle)

    # Return the Group of paddles
    return paddles


def create_ball():
    print("Hello")


def check_keydown_events():
    print("Hello")


def check_keyup_events():
    print("Hello")


def check_events():
    print("Hello")


def check_play_button():
    print("Hello")


def update_screen():
    print("Hello")


def check_ball_paddle_collisions():
    print("Hello")


def ball_hit():
    print("Hello")