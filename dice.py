from random import randint
import pygame


class Dice:
    def __init__(self, screen_size: tuple):
        self.value = 0
        for i in range(6):
            pygame.image.save(pygame.transform.scale(pygame.image.load(f'img/dice/original/{i+1}.png'),
                                                     (screen_size[0] / 20, screen_size[1] / 11.25)),
                              f'img/dice/{i+1}.png')
        self.image = 'img/dice/6.png'

    def roll(self):
        self.value = randint(1, 6)
        if self.value == 1:
            self.image = pygame.image.load('img/dice/1.png')
        elif self.value == 2:
            self.image = pygame.image.load('img/dice/2.png')
        elif self.value == 3:
            self.image = pygame.image.load('img/dice/3.png')
        elif self.value == 4:
            self.image = pygame.image.load('img/dice/4.png')
        elif self.value == 5:
            self.image = pygame.image.load('img/dice/5.png')
        else:
            self.image = pygame.image.load('img/dice/6.png')
