from GUI.main import GUI, pygame
from backgammon import Backgammon
from piece import Piece
from button import Button
from tkinter.messagebox import askyesno


class Game(GUI, Backgammon):
    def __init__(self, mode):
        GUI.__init__(self)
        Backgammon.__init__(self, mode)
        self.is_dragging = False

        self.dice_button = Button(self.screen, (self.width // 2 - self.width // 20,
                                                self.height // 2 - self.height // 30), self.width // 10,
                                  self.height // 15, 'black', 'Dice Roll')
        self.dice_image = Button(self.screen, (self.width // 2 - self.width // 40,
                                               self.height // 2 - self.height // 5),
                                 image=(pygame.image.load(self.dice[0].image))), Button(
            self.screen, (self.width // 2 - self.width // 40, self.height // 2 + self.height // 5 - self.width // 20),
            image=pygame.image.load(self.dice[1].image))

        self.init_board()

    def init_board(self):
        white_checker = pygame.transform.scale(pygame.image.load('img/white.png'),
                                               (self.width // 20, self.height // 12))
        blue_checker = pygame.transform.scale(pygame.image.load('img/blue.png'),
                                              (self.width // 20, self.height // 12))

        checker_images = {0: white_checker, 1: blue_checker}

        for column in range(24):
            piece_capture = []
            amount, player = self.pieces[column][0], self.pieces[column][1]
            for row in range(amount):
                piece_capture.append(Button(self.screen, self.get_specified_coord(column, row),
                                            checker_images[player].get_width(),
                                            checker_images[player].get_height(),
                                            image=checker_images[player]))
            self.pieces[column] = Piece(player=player, column=column,
                                        coord=list(self.get_coord(column)), capture=piece_capture)

    def get_specified_coord(self, column, row):
        if column < 6:
            x = self.width - self.width // 16 - column * 100
        elif column < 12:
            x = self.width - self.width // 20 - (column + 1) * 100
        elif column < 18:
            x = self.width // 80 + column % 12 * 100
        else:
            x = (column % 12 + 1) * 100
        if column < 12:
            y = row * self.height // 12
        else:
            y = self.height - (row + 1) * self.height // 12

        return x, y

    def get_coord(self, column):
        for row in range(5):
            if column < 6:
                x = self.width - self.width // 16 - column * 100
            elif column < 12:
                x = self.width - self.width // 20 - (column + 1) * 100
            elif column < 18:
                x = self.width // 80 + column % 12 * 100
            else:
                x = (column % 12 + 1) * 100
            if column < 12:
                y = row * self.height // 12
            else:
                y = self.height - (row + 1) * self.height // 12

            yield x, y

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
            if event.button == 2:
                if self.check_bearing_off():
                    if self.mouse[1] < self.height // 2:
                        for item in self.pieces[:12]:
                            if item.capture:
                                if item.capture[-1].touched(self.mouse):
                                    if self.player == item.player:
                                        if askyesno('Bearing off', 'Are you sure?'):
                                            item.capture.remove(item.capture[-1])
                                            self.moves.remove(min(self.moves))
                    else:
                        for item in self.pieces[12:]:
                            if item.capture:
                                if item.capture[-1].touched(self.mouse):
                                    if self.player == item.player:
                                        if askyesno('Bearing off', 'Are you sure?'):
                                            item.capture.remove(item.capture[-1])
                                            self.moves.remove(min(self.moves))

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
