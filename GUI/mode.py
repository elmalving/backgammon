from GUI.main import GUI, pygame
from button import Button


class Mode(GUI):
    def __init__(self):
        super().__init__()
        self.duo_button = Button(self.screen, (self.first_row, self.first_col), self.width // 3, self.height // 3,
                                 image=pygame.image.load('img/duo.png'))
        self.computer_button = Button(self.screen, (self.second_row, self.first_col), self.width // 3, self.height // 3,
                                      image=pygame.image.load('img/computer.png'))

    def load(self):
        self.screen.fill('white')

        self.duo_button.create_rect()
        self.computer_button.create_rect()

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
                    if self.duo_button.touched(self.mouse):
                        self.current_window = 'duo'
                        return
                    if self.computer_button.touched(self.mouse):
                        self.current_window = 'computer'
                        return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.current_window = 'Menu'
                        return

            pygame.display.update()
            pygame.time.Clock().tick(30)
