from GUI.main import GUI, pygame
from button import Button


class Menu(GUI):
    def __init__(self):
        super().__init__()
        self.stat_button = Button(self.screen, (self.first_row, self.first_col), self.width // 4, self.height // 4,
                                  image=pygame.image.load('img/stats_button.png'))
        self.mode_button = Button(self.screen, (self.second_row, self.first_col), self.width // 4, self.height // 4,
                                  image=pygame.image.load('img/mode_button.png'))

    def load(self):
        self.screen.fill('black')

        self.stat_button.create_rect()
        self.mode_button.create_rect()

        pygame.display.update()

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load('sound/menu.mp3')
            pygame.mixer.music.play(-1)

    def show(self):
        self.load()
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.stat_button.touched(self.mouse):
                        self.current_window = 'Stats'
                        return
                    elif self.mode_button.touched(self.mouse):
                        self.current_window = 'Mode'
                        return
                if event.type == pygame.MOUSEMOTION:
                    if self.stat_button.touched(self.mouse):
                        if not self.stat_button.colored:
                            self.stat_button.image = pygame.image.load('img/stats_button_hover.png')
                            self.stat_button.create_rect()
                            self.stat_button.colored = True
                    elif self.stat_button.colored:
                        self.stat_button.image = pygame.image.load('img/stats_button.png')
                        self.stat_button.create_rect()
                        self.stat_button.colored = False
                    if self.mode_button.touched(self.mouse):
                        if not self.mode_button.colored:
                            self.mode_button.image = pygame.image.load('img/mode_button_hover.png')
                            self.mode_button.create_rect()
                            self.mode_button.colored = True
                    elif self.mode_button.colored:
                        self.mode_button.image = pygame.image.load('img/mode_button.png')
                        self.mode_button.create_rect()
                        self.mode_button.colored = False

            pygame.display.update()
            pygame.time.Clock().tick(30)
