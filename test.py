width = 1280
height = 720

test = {'single': None}
test['single'] = [1, 2]
test['multi'] = 5
test.pop('multi')
print(test)
# def get_specified_coord(column):
#     if column < 6:
#         x = 1200 - column * 100
#     elif column < 12:
#         x = 16 + 1200 - (column+1) * 100
#     elif column < 18:
#         x = 16 + column % 12 * 100
#     else:
#         x = ((column % 12)+1) * 100
#     return x
#
#
# print(get_specified_coord(18))


# class Test(GUI):
#     def __init__(self):
#         super().__init__()
#         bg = pygame.transform.scale(pygame.image.load('img/backgammon.png'), (self.width, self.height))
#         self.screen.blit(bg, (0, 0))
#         white_checker = pygame.transform.scale(pygame.image.load('img/white.png'),
#                                                (self.width // 20, self.height // 12))
#         self.screen.blit(white_checker, (self.get_x(18), 0))
#         pygame.display.update()
#
#         while self.running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     pass
#                 if event.type == pygame.MOUSEMOTION:
#                     pass
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_ESCAPE:
#                         self.current_window = 'Menu'
#                         return
#             pygame.time.Clock().tick(10)
#
#     def get_x(self, column):
#         if column%12 > 5:
#             x = 16 + (11 - column%12) * 100
#         else:
#             x = 1200 -(column%12) * 100
#         return x
#
#
# test = Test()
