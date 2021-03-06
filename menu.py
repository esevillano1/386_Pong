import pygame
from button import Button
from pygame.sprite import Group
import time

class Menu:
    def __init__(self, settings, screen):
        # Menu Options
        self.settings = settings
        self.screen = screen
        self.width = self.settings.screen_width
        self.height = self.settings.screen_height
        self.options = ["Easy", "Average", "Difficult"]
        self.scores = [7, 11, 15, 21]
        self.difficultyChoice = "Easy"
        self.scoreChoice = 7
        self.font_size = 32
        self.difficultyButtons = Group()
        self.scoreButtons = Group()

    def start_menu(self, settings, screen, play_button):

        # Start at one-sixth of the screen
        startingPoint = 6

        title_font = pygame.font.SysFont(None, 128)
        title = title_font.render("Pong", True, (255, 255, 255))
        ai_font = pygame.font.SysFont(None, 96)
        nextLine = ai_font.render("AI -- NO WALLS", True, (25, 230, 25))
        font = pygame.font.SysFont(None, 32)
        difficulty = font.render("Difficulty Level:", True, (240, 240, 240))
        playTo = font.render("Play up to:", True, (240, 240, 240))

        # Blit the title
        self.screen.fill((0, 0, 0), pygame.Rect(0, 0, self.width, self.height))
        self.screen.blit(title, (self.width/startingPoint, self.height/12))
        self.screen.blit(nextLine, (self.width / startingPoint, self.height / 4))

        # Blit the play game button
        play_button.draw_button()

        # # Blit the difficulty options
        # self.screen.blit(difficulty, (self.width / startingPoint, (self.height * 4)/ 6))
        #
        # # Reset the startingPoint
        # point = (self.width / startingPoint) * 2.5
        #
        # for option in self.options:
        #     if self.difficultyChoice == option:
        #         self.color = (255, 0, 0)
        #     else:
        #         self.color = (240, 240, 240)
        #     difficulty_button = Button(settings, screen, str(option), point, ((self.height * 4) / 6), self.color, self.font_size)
        #     difficulty_button.draw_button()
        #     point *= 1.3
        #
        #     if not self.difficultyButtons.has(difficulty_button):
        #         self.difficultyButtons.add(difficulty_button)
        #
        # # Reset the startingPoint
        # point = startingPoint
        #
        # # Blit the score options
        # self.screen.blit(playTo, (self.width / point, (self.height * 7) / 8))
        # point = (self.width / point) * 1.9
        # for score in self.scores:
        #     if self.scoreChoice == score:
        #         self.color = (255, 0, 0)
        #     else:
        #         self.color = (240, 240, 240)
        #
        #     score_button = Button(settings, screen, str(score), point, ((self.height * 7) / 8), self.color, self.font_size)
        #     score_button.draw_button()
        #     point *= 1.15
        #
        #     if not self.scoreButtons.has(score_button):
        #         self.scoreButtons.add(score_button)
        #
        #
        # # Reset the startingPoint
        # startingPoint = 6

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def changeOption(self, mouse_x, mouse_y):
        for button in self.difficultyButtons:
            if button.rect.x == mouse_x and button.rect.y == mouse_y:
                self.difficultyChoice = button.msg

        for button in self.scoreButtons:
            if button.rect.x == mouse_x and button.rect.y == mouse_y:
                self.scoreChoice = int(button.msg)

    def game_won(self, settings, stats):
        winner = pygame.font.SysFont(None, 128)
        if stats.player_score == settings.winning_score:
            msg = "Player Won!!!"
        elif stats.ai_score == settings.winning_score:
            msg = "AI Won..."

        title = winner.render(msg, True, (255, 255, 255))

        # Blit the title
        self.screen.blit(title, (self.width/6, self.height/4))
        pygame.display.flip()

        # Pause the game to show who won
        time.sleep(5)

        # Hide the mouse cursor.
        pygame.mouse.set_visible(True)

        # Reset the game state to inactive
        stats.game_active = False
