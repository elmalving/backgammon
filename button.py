import pygame


class Button:
    def __init__(self, screen, coord: tuple, width: int = 0, height: int = 0, color='black', text: str = None,
                 text_color='white', font: str = 'bahnschrift', font_size: int = 30, only_text: bool = None,
                 image=None):
        self.screen = screen
        self.color = color
        self.x = coord[0]
        self.y = coord[1]
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.font_size = font_size
        self.only_text = only_text
        self.image = image
        self.colored = False

    def move(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def create_rect(self, outline=None, border_radius: int = 0):
        if not self.only_text:
            if outline:
                pygame.draw.rect(self.screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4),
                                 border_radius=border_radius)
            if self.image:
                self.screen.blit(self.image, self.image.get_rect(x=self.x, y=self.y))
            else:
                pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), 0,
                                 border_radius=border_radius)

        if self.text:
            font = pygame.font.SysFont(self.font, self.font_size)
            text = font.render(self.text, True, self.text_color)
            self.screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                                    self.y + (self.height / 2 - text.get_height() / 2)))

    def touched(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True

        return False
