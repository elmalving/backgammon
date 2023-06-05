import pygame
import sqlite3


class GUI:
    def __init__(self):
        pygame.init()
        pygame.display.set_icon(pygame.image.load('img/icon.png'))
        pygame.display.set_caption("Backgammon")
        self.db = sqlite3.connect('../info.db')
        self.cursor = self.db.cursor()
        self.screen = pygame.display.set_mode((1280, 720))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.first_row = self.width // 6
        self.second_row = self.width // 1.7
        self.first_col = self.height // 8
        self.second_col = self.height // 2
        self.current_window = None
        self.running = True

    @property
    def mouse(self):
        return pygame.mouse.get_pos()
