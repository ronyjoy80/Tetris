import random

import pygame.sprite

from square import Square


class Tetromino_I:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        self.tetromino = []
        for i in range(3, 7):
            self.tetromino.append(Square(i, 0, cell_points_gap, square_length, cell_start_point))

    def rotate(self):
        pass


class Tetromino_O:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        self.tetromino = []
        for i in range(4, 6):
            for j in range(2):
                self.tetromino.append(Square(i, j, cell_points_gap, square_length, cell_start_point))

    def rotate(self):
        pass


class Tetromino_T:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = []
        for i in range(3, 6):
            self.tetromino.append(Square(offset + i, 0, cell_points_gap, square_length, cell_start_point))
        self.tetromino.append(Square(offset + 4, 1, cell_points_gap, square_length, cell_start_point))

    def rotate(self):
        pass


class Tetromino_J:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = []
        for i in range(3, 6):
            self.tetromino.append(Square(offset + i, 0, cell_points_gap, square_length, cell_start_point))
        self.tetromino.append(Square(offset + 5, 1, cell_points_gap, square_length, cell_start_point))

    def rotate(self):
        pass


class Tetromino_L:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = []
        for i in range(3, 6):
            self.tetromino.append(Square(offset + i, 0, cell_points_gap, square_length, cell_start_point))
        self.tetromino.append(Square(offset + 3, 1, cell_points_gap, square_length, cell_start_point))

    def rotate(self):
        pass


class Tetromino_S:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = [
            Square(offset + 4, 0, cell_points_gap, square_length, cell_start_point),
            Square(offset + 5, 0, cell_points_gap, square_length, cell_start_point),
            Square(offset + 3, 1, cell_points_gap, square_length, cell_start_point),
            Square(offset + 4, 1, cell_points_gap, square_length, cell_start_point)
        ]

    def rotate(self):
        pass


class Tetromino_Z:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = [
            Square(offset + 3, 0, cell_points_gap, square_length, cell_start_point),
            Square(offset + 4, 0, cell_points_gap, square_length, cell_start_point),
            Square(offset + 4, 1, cell_points_gap, square_length, cell_start_point),
            Square(offset + 5, 1, cell_points_gap, square_length, cell_start_point)
        ]

    def rotate(self):
        pass


class Tetromino(pygame.sprite.Group):
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        super().__init__()
        self.random_tetromino = random.choice([Tetromino_Z, Tetromino_O, Tetromino_I, Tetromino_J,
                                               Tetromino_L, Tetromino_S,
                                               Tetromino_T])(cell_points_gap, square_length, cell_start_point)
        self.add(self.random_tetromino.tetromino)

    def rotate(self):
        self.random_tetromino.rotate()
