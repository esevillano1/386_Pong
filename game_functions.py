import pygame
import random
from pygame.sprite import Group
import sys
from pygame.mixer import music

from ball import Ball
from paddle import Paddle


def create_paddles(settings, screen, paddles, ai_paddles):
    # Create the player paddles
    playerLeftPaddle = Paddle(settings, screen, "left", "player")
    playerTopPaddle = Paddle(settings, screen, "top", "player")
    playerBottomPaddle = Paddle(settings, screen, "bottom", "player")

    # Create the three ai paddles
    aiRightPaddle = Paddle(settings, screen, "right", "ai")
    aiTopPaddle = Paddle(settings, screen, "top", "ai")
    aiBottomPaddle = Paddle(settings, screen, "bottom", "ai")

    # Add all the paddles to the sprite Group
    paddles.add(playerLeftPaddle)
    paddles.add(playerTopPaddle)
    paddles.add(playerBottomPaddle)
    paddles.add(aiRightPaddle)
    paddles.add(aiTopPaddle)
    paddles.add(aiBottomPaddle)

    # Add the ai paddles to their own sprite Group
    ai_paddles.add(aiRightPaddle)
    ai_paddles.add(aiTopPaddle)
    ai_paddles.add(aiBottomPaddle)


def create_center_line(settings, screen):
    firstPos = (settings.screen_width / 2, 0)
    newPos = (settings.screen_width / 2, settings.screen_height)
    pygame.draw.line(screen, settings.white, firstPos, newPos)


def check_keydown_events(paddles):
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


def check_events(settings, screen, stats, sb, menu, play_button, ball, paddles):
    if stats.game_active is False:
        menu.start_menu(settings, screen, play_button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddles)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(paddles)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            menu.changeOption(mouse_x, mouse_y)
            check_play_button(settings, stats, sb, play_button, mouse_x, mouse_y)

    # Check for any collision
    check_ball_paddle_collisions(settings, ball, paddles)


def check_play_button(settings, stats, sb, play_button, mouse_x, mouse_y):
    """Start a new game when the player clicks Play Game."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()


def check_ball_paddle_collisions(settings, ball, paddles):
    for paddle in paddles:
        if ball.location.colliderect(paddle.location):
            ball_sound_effect()
            ball_hit(settings, ball, paddle)
            

def ball_sound_effect():
    pygame.mixer.music.load('audio/ball_hit.mp3')
    pygame.mixer.music.play(0)


def reset_ball(settings, ball):
    # Reset the location of the ball
    ball.location.x = settings.screen_width/2
    ball.location.y = settings.screen_height/2
    directions = [-1, 1]
    ball.xdir = directions[random.randint(0, 1)]
    ball.ydir = directions[random.randint(0, 1)]
    while settings.ball_speed_x == 0 and settings.ball_speed_y == 0:
        settings.ball_speed_x = random.uniform(-1, 1)
        settings.ball_speed_y = random.uniform(-1, 1)


def increase_point(settings, stats, sb, ball):
    # Check if the ball went past the ai out of bounds
    if ball.location.x > settings.screen_width/2:
        if ball.location.y < 0 or ball.location.y > settings.screen_height or ball.location.x > settings.screen_width:
            stats.player_score += 1
            reset_ball(settings, ball)
    # Check if the ball went past the player out of bounds
    else:
        if ball.location.y < 0 or ball.location.y > settings.screen_height or ball.location.x < 0:
            stats.ai_score += 1
            reset_ball(settings, ball)

    # Render the new score to be updated on the board
    sb.prep_score()


def ball_hit(settings, ball, paddle):
    # Values used for comparison
    x = ball.location.x
    y = ball.location.y
    top_third_vert = paddle.location.y + settings.paddleSize/3
    middle_third_vert = paddle.location.y + (settings.paddleSize * 2)/3
    bottom_third_vert = paddle.location.y + settings.paddleSize
    left_third_hor = paddle.location.x + settings.paddleSize/3
    middle_third_hor = paddle.location.x + (settings.paddleSize * 2)/3
    right_third_hor = paddle.location.x + settings.paddleSize

    if paddle.wall == "left" or paddle.wall == "right":
        if paddle.location.y <= y < top_third_vert:
            settings.ball_speed_x = 1
            settings.ball_speed_y = 1.2
        elif top_third_vert <= y < middle_third_vert:
            settings.ball_speed_x = 1.5
            settings.ball_speed_y = 2
        elif middle_third_vert <= y <= bottom_third_vert:
            settings.ball_speed_x = 1.7
            settings.ball_speed_y = 2.5
        ball.xdir *= -1
    elif paddle.wall == "top" or paddle.wall == "bottom":
        if paddle.location.x <= x < left_third_hor:
            settings.ball_speed_x = 1.2
            settings.ball_speed_y = 1
        elif left_third_hor <= x < middle_third_hor:
            settings.ball_speed_x = 2
            settings.ball_speed_y = 1.5
        elif middle_third_hor <= x <= right_third_hor:
            settings.ball_speed_x = 2.5
            settings.ball_speed_y = 1.7
        ball.ydir *= -1


def ai_paddle_move(settings, screen, ball, paddle):
    """Move the paddles based on the x and y location of the ball."""
    difficulty = 3
    paddle_x = paddle.location.x + settings.paddleSize
    width = settings.screen_width
    if paddle.wall == "top" or paddle.wall == "bottom" and paddle_x < ball.location.x and width/2 <= paddle_x < width:
        paddle.location.x += (int(settings.ball_speed_x/difficulty) * ball.xdir)
    pygame.draw.rect(screen, settings.white, paddle.location)

def update_screen(settings, screen, stats, sb, ball, paddles, ai_paddles):
    # Redraw the screen during each pass through the loop
    screen.fill(settings.black)

    # Draw the center line
    create_center_line(settings, screen)

    # Draw the score information
    sb.show_score()

    # Update the position of the ball
    pygame.draw.rect(screen, settings.white, ball.location)
    ball.update()

    for paddle in ai_paddles:
        ai_paddle_move(settings, screen, ball, paddle)

    for paddle in paddles:
        if paddle.user != "ai":
            pygame.draw.rect(screen, settings.white, paddle.location)
            paddle.update()

    # Make the most recently drawn screen visible
    pygame.display.update()


def win_condition(settings, stats, menu):
    if settings.winning_score == stats.player_score or settings.winning_score == stats.ai_score:
        menu.game_won(settings, stats)
