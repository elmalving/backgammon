from button import Button


class Piece:
    def __init__(self, player: int, column: int, coord: [tuple], capture: [Button]):
        self.player = player
        self.column = column
        self.coord = coord
        self.capture = capture

    @property
    def amount(self):
        return len(self.capture)
