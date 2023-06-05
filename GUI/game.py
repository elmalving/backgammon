import pygame
from backgammon import Backgammon
from button import Button
from tkinter.messagebox import askyesno


class Game(Backgammon):
    def __init__(self, mode):
        super().__init__(mode)
        self.is_dragging = False

        self.dice_button = Button(self.screen, (self.width // 2 - self.width // 20,
                                                self.height // 2 - self.height // 30), self.width // 10,
                                  self.height // 15, 'black', 'Dice Roll')
        self.dice_image = Button(self.screen, (self.width // 2 - self.width // 40,
                                               self.height // 2 - self.height // 5),
                                 image=(pygame.image.load(self.dice[0].image))), Button(
            self.screen, (self.width // 2 - self.width // 40, self.height // 2 + self.height // 5 - self.width // 20),
            image=pygame.image.load(self.dice[1].image))

    def load(self):
        bg = pygame.transform.scale(pygame.image.load('img/backgammon.png'), (self.width, self.height))
        self.screen.blit(bg, (0, 0))

        self.dice_button.create_rect(border_radius=10, outline='black')
        for dice in self.dice_image:
            dice.create_rect()

        for piece in self.pieces:
            if piece.capture:
                for checker in piece.capture:
                    checker.create_rect()

    def handle_dragging(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rolled:
                if self.mouse[1] < self.height // 2:
                    for item in self.pieces[:12]:
                        if item.capture:
                            if item.capture[-1].touched(self.mouse):
                                if self.player == item.player:
                                    self.is_dragging = True
                                    self.dragging_block = item
                else:
                    for item in self.pieces[12:]:
                        if item.capture:
                            if item.capture[-1].touched(self.mouse):
                                if self.player == item.player:
                                    self.is_dragging = True
                                    self.dragging_block = item
            # if event.button == 2:
            #     if self.check_bearing_off():
            #         if self.mouse[1] < self.height // 2:
            #             for item in self.pieces[:12]:
            #                 if item.capture:
            #                     if item.capture[-1].touched(self.mouse):
            #                         if self.player == item.player:
            #                             if askyesno('Bearing off', 'Are you sure?'):
            #                                 item.capture.remove(item.capture[-1])
            #                                 self.moves.remove(min(self.moves))
            #         else:
            #             for item in self.pieces[12:]:
            #                 if item.capture:
            #                     if item.capture[-1].touched(self.mouse):
            #                         if self.player == item.player:
            #                             if askyesno('Bearing off', 'Are you sure?'):
            #                                 item.capture.remove(item.capture[-1])
            #                                 self.moves.remove(min(self.moves))

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.is_dragging:
                self.is_dragging = False
                self.move()
                self.load()

        elif event.type == pygame.MOUSEMOTION:
            if self.is_dragging:
                checker = self.dragging_block.capture[-1]
                checker.move((self.mouse[0] - checker.width // 2, self.mouse[1] - checker.height // 2))
                self.load()

    def handle_dice(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.dice_button.touched(self.mouse):
                self.roll()
                for i in range(2):
                    self.dice_image[i].image = self.dice[i].image
                self.load()
        if event.type == pygame.MOUSEMOTION:
            if self.dice_button.touched(self.mouse):
                self.dice_button.color = 'grey'
                self.dice_button.colored = True
                self.dice_button.create_rect(border_radius=10, outline='black')
            elif self.dice_button.colored:
                self.dice_button.color = 'black'
                self.dice_button.colored = False
                self.dice_button.create_rect(border_radius=10, outline='black')

    def show(self):
        self.load()
        pygame.mixer.music.load('sound/game.mp3')
        pygame.mixer.music.play(-1)
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if askyesno('Confirm', 'Are you sure you want to leave?'):
                            pygame.mixer.music.stop()
                            self.current_window = 'Mode'
                            return

                self.handle_dragging(event)
                self.handle_dice(event)

            pygame.display.update()
            pygame.time.Clock().tick(30)
