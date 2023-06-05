from GUI.main import GUI, pygame


class Stats(GUI):
    def __init__(self):
        super().__init__()

    def load(self):
        self.screen.fill('black')

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
                    pass
                if event.type == pygame.MOUSEMOTION:
                    pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.current_window = 'Menu'
                        return

            pygame.display.update()
            pygame.time.Clock().tick(30)
