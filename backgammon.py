import pygame
from dice import Dice


class Backgammon:
    def __init__(self, mode):
        self.mode = mode
        self.player = 1
        self.rolled = False
        self.moves = []
        self.dragging_block = None
        self.lost_checker = None
        self.dice = (Dice(self.screen.get_size()), Dice(self.screen.get_size()))
        self.pieces = list([(0, None)] * 24)
        self.pieces[5] = self.pieces[12] = (5, 1)
        self.pieces[0] = (2, 0)
        self.pieces[7] = (3, 1)
        self.pieces[11] = self.pieces[18] = (5, 0)
        self.pieces[16] = (3, 0)
        self.pieces[23] = (2, 1)

    def roll(self):
        if not self.rolled:
            for dice in self.dice:
                dice.roll()
                self.moves.append(dice.value)
            self.rolled = True

    def move(self):
        checker = self.dragging_block.capture[-1]
        moves = self.find_possible_moves()
        collision = self.check_collision(checker, moves)
        if collision:
            checker.move(collision[0])
            if moves['special'] == collision[1].column or moves['second_special'] == collision[1].column:
                collision[1].capture.clear()
            collision[1].capture.append(checker)
            collision[1].player = self.dragging_block.player
            self.dragging_block.capture.remove(checker)
            if self.dragging_block.amount == 0:
                self.dragging_block.player = None
            if self.player == 0:
                if collision[1].column - self.dragging_block.column in self.moves:
                    self.moves.remove(collision[1].column - self.dragging_block.column)
                else:
                    self.moves.clear()
            else:
                if self.dragging_block.column - collision[1].column in self.moves:
                    self.moves.remove(self.dragging_block.column - collision[1].column)
                else:
                    self.moves.clear()
            if not self.moves:
                self.player ^= 1
                self.rolled = False
        else:
            checker.move(self.dragging_block.coord[self.dragging_block.amount - 1])

    def check_collision(self, checker, moves):
        dragging_rect = pygame.Rect(checker.x, checker.y, checker.width, checker.height)
        for move in moves.values():
            if move is not None:
                block = self.pieces[move]
                if moves['special'] == block.column or moves['second_special'] == block.column:
                    x = block.coord[1][0]
                    y = block.coord[1][1]
                    collide_rect = pygame.Rect(x, y, checker.width, checker.height)
                    if dragging_rect.colliderect(collide_rect):
                        return (block.coord[0][0], block.coord[0][1]), block
                else:
                    x = block.coord[block.amount][0]
                    y = block.coord[block.amount][1]

                collide_rect = pygame.Rect(x, y, checker.width, checker.height)
                if dragging_rect.colliderect(collide_rect):
                    return (x, y), block

    def find_possible_moves(self):
        possible_moves = []
        moves = {'first': None, 'second': None, 'double_dice': None, 'special': None, 'second_special': None}
        for i in range(len(self.moves)):
            if self.player == 0:
                possible_moves.append(self.dragging_block.column + self.moves[i])
                if i > 0:
                    possible_moves.append(self.dragging_block.column + self.moves[i] + self.moves[i-1])
            else:
                possible_moves.append(self.dragging_block.column - self.moves[i])
                if i > 0:
                    possible_moves.append(self.dragging_block.column - self.moves[i] - self.moves[i-1])

        for block in self.pieces:
            if block.column in possible_moves:
                if block.player != self.player and block.player is not None:
                    if block.amount == 1:
                        if moves['special'] is None:
                            moves['special'] = block.column
                        else:
                            moves['second_special'] = block.column
                        continue
                else:
                    if block.amount != 5:
                        if len(self.moves) > 1:
                            if block.column == possible_moves[-1]:
                                moves['double_dice'] = possible_moves[-1]
                                continue
                        if moves['first'] is None:
                            moves['first'] = block.column
                        else:
                            moves['second'] = block.column
        return moves

    def check_bearing_off(self):
        bearing_off = True
        for piece in self.pieces:
            if self.player == 0:
                if piece.column < 18 and piece.capture and piece.player == self.player:
                    bearing_off = False
            else:
                if piece.column > 5 and piece.capture and piece.player == self.player:
                    bearing_off = False

        return bearing_off
