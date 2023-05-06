import random
import numpy as np
import pygame.sprite

from square import Square


class Tetromino_I:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        self.tetromino = []
        for i in range(3, 7):
            self.tetromino.append(Square(i, 0, cell_points_gap, square_length, cell_start_point))
        self.rotate_position = 0
        self.rotation = [
            np.array([[1, -1], [0, 0], [-1, 1], [-2, 2]]),
            np.array([[-1, 2], [0, 1], [1, 0], [2, -1]]),
            np.array([[2, -2], [1, -1], [0, 0], [-1, 1]]),
            np.array([[-2, 1], [-1, 0], [0, -1], [1, -2]])
        ]
        self.rotation_steps = len(self.rotation)


class Tetromino_O:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        self.tetromino = []
        for i in range(4, 6):
            for j in range(2):
                self.tetromino.append(Square(i, j, cell_points_gap, square_length, cell_start_point))
        self.rotate_position = 0
        self.rotation = [np.array([[0, 0], [0, 0], [0, 0], [0, 0]])]
        self.rotation_steps = len(self.rotation)


class Tetromino_T:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = []
        for i in range(3, 6):
            self.tetromino.append(Square(offset + i, 0, cell_points_gap, square_length, cell_start_point))
        self.tetromino.append(Square(offset + 4, 1, cell_points_gap, square_length, cell_start_point))
        self.rotate_position = 0
        self.rotation = [
            np.array([[1, -1], [0, 0], [0, 0], [0, 0]]),
            np.array([[-1, 1], [0, -1], [0, -1], [0, 0]]),
            np.array([[0, 0], [0, 0], [0, 0], [-1, 1]]),
            np.array([[0, 0], [0, 1], [0, 1], [1, -1]])
        ]
        self.rotation_steps = len(self.rotation)


class Tetromino_J:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = []
        for i in range(3, 6):
            self.tetromino.append(Square(offset + i, 0, cell_points_gap, square_length, cell_start_point))
        self.tetromino.append(Square(offset + 5, 1, cell_points_gap, square_length, cell_start_point))
        self.rotate_position = 0
        self.rotation = [
            np.array([[0, 0], [-1, 1], [-2, 2], [-1, -1]]),
            np.array([[0, 1], [0, 1], [1, 0], [1, 2]]),
            np.array([[1, 1], [2, -2], [1, -1], [0, 0]]),
            np.array([[-1, -2], [-1, 0], [0, -1], [0, -1]])
        ]
        self.rotation_steps = len(self.rotation)


class Tetromino_L:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = []
        for i in range(3, 6):
            self.tetromino.append(Square(offset + i, 0, cell_points_gap, square_length, cell_start_point))
        self.tetromino.append(Square(offset + 3, 1, cell_points_gap, square_length, cell_start_point))
        self.rotate_position = 0
        self.rotation = [
            np.array([[0, 0], [0, 0], [-1, 2], [-1, 2]]),
            np.array([[0, 2], [1, 1], [2, -1], [1, 0]]),
            np.array([[1, -2], [1, -2], [0, 0], [0, 0]]),
            np.array([[-1, 0], [-2, 1], [-1, -1], [0, -2]])
        ]
        self.rotation_steps = len(self.rotation)


class Tetromino_S:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = [
            Square(offset + 4, 0, cell_points_gap, square_length, cell_start_point),
            Square(offset + 5, 0, cell_points_gap, square_length, cell_start_point),
            Square(offset + 3, 1, cell_points_gap, square_length, cell_start_point),
            Square(offset + 4, 1, cell_points_gap, square_length, cell_start_point)
        ]
        self.rotate_position = 0
        self.rotation = [
            np.array([[0, -1], [-1, 1], [0, 0], [-1, 2]]),
            np.array([[0, 2], [1, 0], [0, 1], [1, -1]]),
            np.array([[1, -2], [0, 0], [1, -1], [0, 1]]),
            np.array([[-1, 1], [0, -1], [-1, 0], [0, -2]])
        ]
        self.rotation_steps = len(self.rotation)


class Tetromino_Z:
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        offset = random.randrange(0, 2)
        self.tetromino = [
            Square(offset + 3, 0, cell_points_gap, square_length, cell_start_point),
            Square(offset + 4, 0, cell_points_gap, square_length, cell_start_point),
            Square(offset + 4, 1, cell_points_gap, square_length, cell_start_point),
            Square(offset + 5, 1, cell_points_gap, square_length, cell_start_point)
        ]
        self.rotate_position = 0
        self.rotation = [
            np.array([[0, 1], [-1, 2], [0, -1], [-1, 0]]),
            np.array([[0, 0], [1, -1], [0, 2], [1, 1]]),
            np.array([[1, 0], [0, 1], [1, -2], [0, -1]]),
            np.array([[-1, -1], [0, -2], [-1, 1], [0, 0]])
        ]
        self.rotation_steps = len(self.rotation)


class Tetromino(pygame.sprite.Group):
    def __init__(self, cell_points_gap, square_length, cell_start_point):
        super().__init__()
        self.movement = True
        self.collision = False
        self.updated_sprites = []
        self.count_sprite_update = 0
        self.random_tetromino = random.choice([Tetromino_Z, Tetromino_O, Tetromino_I, Tetromino_J,
                                               Tetromino_L, Tetromino_S,
                                               Tetromino_T])(cell_points_gap, square_length, cell_start_point)
        # self.random_tetromino = Tetromino_L(cell_points_gap, square_length, cell_start_point)
        self.add(self.random_tetromino.tetromino)
        self.prev = None

    def rotate(self, square_group):
        list_xy = np.array(sorted([(square.grid_pos_x, square.grid_pos_y)
                                   for square in self.random_tetromino.tetromino]))
        # print(list_xy)
        rotated_list_xy = np.add(list_xy, self.random_tetromino.rotation[self.random_tetromino.rotate_position])
        for i in range(4):
            if self.random_tetromino.tetromino[i].set_xy(rotated_list_xy[i][0], rotated_list_xy[i][1], square_group):
                for j in range(4):
                    self.random_tetromino.tetromino[j].set_xy(list_xy[j][0], list_xy[j][1], SquareRowGroup())
                return
        self.random_tetromino.rotate_position += 1
        self.random_tetromino.rotate_position %= self.random_tetromino.rotation_steps

    def check(self):
        current = np.array(sorted([(square.grid_pos_x, square.grid_pos_y)
                                   for square in self.random_tetromino.tetromino]))
        print(current.tolist())
        if self.prev is None:
            self.prev = current
        else:
            print(np.subtract(current, self.prev).tolist())


class SquareRowGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.movement = False
        self.collision = False
        self.updated_sprites = []
        self.count_sprite_update = 0
        self.num_of_square = 0
