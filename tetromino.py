import random
import numpy as np
import pygame.sprite

from square import Square


# Class of seven different Tetromino
class Tetromino_I:
    def __init__(self, cell_points_gap, square_length, cell_start_point, color, design):
        self.shape = "I"
        self.tetromino = []
        for i in range(4):
            self.tetromino.append(Square(i, 0, cell_points_gap, square_length, cell_start_point, color, design))
        self.rotate_position = 0
        self.rotation = [
            np.array([[1, -1], [0, 0], [-1, 1], [-2, 2]]),
            np.array([[-1, 2], [0, 1], [1, 0], [2, -1]]),
            np.array([[2, -2], [1, -1], [0, 0], [-1, 1]]),
            np.array([[-2, 1], [-1, 0], [0, -1], [1, -2]])
        ]
        self.rotation_steps = len(self.rotation)

    # Function to move tetromino to center of play area
    def move_to_center(self):
        for i in range(4):
            self.tetromino[i].grid_pos_x += 3
            self.tetromino[i].update_rect_topleft()


class Tetromino_O:
    def __init__(self, cell_points_gap, square_length, cell_start_point, color, design):
        self.shape = "O"
        self.tetromino = []
        for i in range(2):
            for j in range(2):
                self.tetromino.append(Square(i, j, cell_points_gap, square_length, cell_start_point, color, design))
        self.rotate_position = 0
        self.rotation = [np.array([[0, 0], [0, 0], [0, 0], [0, 0]])]
        self.rotation_steps = len(self.rotation)

    # Function to move tetromino to center of play area
    def move_to_center(self):
        for i in range(4):
            self.tetromino[i].grid_pos_x += 4
            self.tetromino[i].update_rect_topleft()


class Tetromino_T:
    def __init__(self, cell_points_gap, square_length, cell_start_point, color, design):
        self.shape = "T"
        self.tetromino = []
        for i in range(3):
            self.tetromino.append(Square(i, 0, cell_points_gap, square_length, cell_start_point, color, design))
        self.tetromino.append(Square(1, 1, cell_points_gap, square_length, cell_start_point, color, design))
        self.rotate_position = 0
        self.rotation = [
            np.array([[1, -1], [0, 0], [0, 0], [0, 0]]),
            np.array([[-1, 1], [0, -1], [0, -1], [0, 0]]),
            np.array([[0, 0], [0, 0], [0, 0], [-1, 1]]),
            np.array([[0, 0], [0, 1], [0, 1], [1, -1]])
        ]
        self.rotation_steps = len(self.rotation)

    # Function to move tetromino to center of play area
    def move_to_center(self):
        offset = random.randrange(0, 2)
        for i in range(4):
            self.tetromino[i].grid_pos_x += 3 + offset
            self.tetromino[i].update_rect_topleft()


class Tetromino_J:
    def __init__(self, cell_points_gap, square_length, cell_start_point, color, design):
        self.shape = "J"
        self.tetromino = []
        for i in range(3):
            self.tetromino.append(Square(i, 0, cell_points_gap, square_length, cell_start_point, color, design))
        self.tetromino.append(Square(2, 1, cell_points_gap, square_length, cell_start_point, color, design))
        self.rotate_position = 0
        self.rotation = [
            np.array([[0, 0], [-1, 1], [-2, 2], [-1, -1]]),
            np.array([[0, 1], [0, 1], [1, 0], [1, 2]]),
            np.array([[1, 1], [2, -2], [1, -1], [0, 0]]),
            np.array([[-1, -2], [-1, 0], [0, -1], [0, -1]])
        ]
        self.rotation_steps = len(self.rotation)

    # Function to move tetromino to center of play area
    def move_to_center(self):
        offset = random.randrange(0, 2)
        for i in range(4):
            self.tetromino[i].grid_pos_x += 3 + offset
            self.tetromino[i].update_rect_topleft()


class Tetromino_L:
    def __init__(self, cell_points_gap, square_length, cell_start_point, color, design):
        self.shape = "L"
        self.tetromino = []
        for i in range(3):
            self.tetromino.append(Square(i, 0, cell_points_gap, square_length, cell_start_point, color, design))
        self.tetromino.append(Square(0, 1, cell_points_gap, square_length, cell_start_point, color, design))
        self.rotate_position = 0
        self.rotation = [
            np.array([[0, 0], [0, 0], [-1, 2], [-1, 2]]),
            np.array([[0, 2], [1, 1], [2, -1], [1, 0]]),
            np.array([[1, -2], [1, -2], [0, 0], [0, 0]]),
            np.array([[-1, 0], [-2, 1], [-1, -1], [0, -2]])
        ]
        self.rotation_steps = len(self.rotation)

    # Function to move tetromino to center of play area
    def move_to_center(self):
        offset = random.randrange(0, 2)
        for i in range(4):
            self.tetromino[i].grid_pos_x += 3 + offset
            self.tetromino[i].update_rect_topleft()


class Tetromino_S:
    def __init__(self, cell_points_gap, square_length, cell_start_point, color, design):
        self.shape = "S"
        self.tetromino = [
            Square(1, 0, cell_points_gap, square_length, cell_start_point, color, design),
            Square(2, 0, cell_points_gap, square_length, cell_start_point, color, design),
            Square(0, 1, cell_points_gap, square_length, cell_start_point, color, design),
            Square(1, 1, cell_points_gap, square_length, cell_start_point, color, design)
        ]
        self.rotate_position = 0
        self.rotation = [
            np.array([[0, -1], [-1, 1], [0, 0], [-1, 2]]),
            np.array([[0, 2], [1, 0], [0, 1], [1, -1]]),
            np.array([[1, -2], [0, 0], [1, -1], [0, 1]]),
            np.array([[-1, 1], [0, -1], [-1, 0], [0, -2]])
        ]
        self.rotation_steps = len(self.rotation)

    # Function to move tetromino to center of play area
    def move_to_center(self):
        offset = random.randrange(0, 2)
        for i in range(4):
            self.tetromino[i].grid_pos_x += 3 + offset
            self.tetromino[i].update_rect_topleft()


class Tetromino_Z:
    def __init__(self, cell_points_gap, square_length, cell_start_point, color, design):
        self.shape = "Z"
        self.tetromino = [
            Square(0, 0, cell_points_gap, square_length, cell_start_point, color, design),
            Square(1, 0, cell_points_gap, square_length, cell_start_point, color, design),
            Square(1, 1, cell_points_gap, square_length, cell_start_point, color, design),
            Square(2, 1, cell_points_gap, square_length, cell_start_point, color, design)
        ]
        self.rotate_position = 0
        self.rotation = [
            np.array([[0, 1], [-1, 2], [0, -1], [-1, 0]]),
            np.array([[0, 0], [1, -1], [0, 2], [1, 1]]),
            np.array([[1, 0], [0, 1], [1, -2], [0, -1]]),
            np.array([[-1, -1], [0, -2], [-1, 1], [0, 0]])
        ]
        self.rotation_steps = len(self.rotation)

    # Function to move tetromino to center of play area
    def move_to_center(self):
        offset = random.randrange(0, 2)
        for i in range(4):
            self.tetromino[i].grid_pos_x += 3 + offset
            self.tetromino[i].update_rect_topleft()


# Class to create random tetromino
# this class is a sprite.Group which handles updates of Class Square Objects
class Tetromino(pygame.sprite.Group):
    def __init__(self, cell_points_gap, square_length, grid_start_point, colors,
                 move_to_center=True, shape="RANDOM", sprites=None):
        super().__init__()
        design = (random.randrange(2), random.randrange(2))
        color = colors[design[0]]
        self.grid_start_point = grid_start_point
        self.movement = True
        self.collision = False
        self.failed_to_place = False
        self.updated_sprites = []
        self.count_sprite_update = 0
        if shape == "Z":
            self.tetromino_object = Tetromino_Z(cell_points_gap, square_length, grid_start_point, color, design)
        elif shape == "O":
            self.tetromino_object = Tetromino_O(cell_points_gap, square_length, grid_start_point, color, design)
        elif shape == "I":
            self.tetromino_object = Tetromino_I(cell_points_gap, square_length, grid_start_point, color, design)
        elif shape == "J":
            self.tetromino_object = Tetromino_J(cell_points_gap, square_length, grid_start_point, color, design)
        elif shape == "L":
            self.tetromino_object = Tetromino_L(cell_points_gap, square_length, grid_start_point, color, design)
        elif shape == "S":
            self.tetromino_object = Tetromino_S(cell_points_gap, square_length, grid_start_point, color, design)
        elif shape == "T":
            self.tetromino_object = Tetromino_T(cell_points_gap, square_length, grid_start_point, color, design)
        else:
            self.tetromino_object = random.choice([Tetromino_Z, Tetromino_O, Tetromino_I, Tetromino_J,
                                                   Tetromino_L, Tetromino_S, Tetromino_T
                                                   ])(cell_points_gap, square_length, grid_start_point, color, design)
        # self.random_tetromino = Tetromino_L(cell_points_gap, square_length, cell_start_point)
        # print(self.tetromino_object.shape)
        if move_to_center:
            self.tetromino_object.move_to_center()
        # noinspection PyTypeChecker
        self.add(self.tetromino_object.tetromino)
        if sprites is not None:
            # noinspection PyTypeChecker
            if len(pygame.sprite.groupcollide(self, sprites, False, False)) != 0:
                self.failed_to_place = True
        self.prev = None

    # Function to rotate tetromino
    def rotate(self, square_group):
        list_xy = np.array(sorted([(square.grid_pos_x, square.grid_pos_y)
                                   for square in self.tetromino_object.tetromino]))
        # print(list_xy)
        rotated_list_xy = np.add(list_xy, self.tetromino_object.rotation[self.tetromino_object.rotate_position])
        for i in range(4):
            if self.tetromino_object.tetromino[i].set_xy(rotated_list_xy[i][0], rotated_list_xy[i][1], square_group):
                for j in range(4):
                    self.tetromino_object.tetromino[j].set_xy(list_xy[j][0], list_xy[j][1], SquareRowGroup())
                return
        self.tetromino_object.rotate_position += 1
        self.tetromino_object.rotate_position %= self.tetromino_object.rotation_steps

    # return type of the tetromino
    def get_shape(self):
        return self.tetromino_object.shape

    # part of Cheat Function
    def check(self):
        current = np.array(sorted([(square.grid_pos_x, square.grid_pos_y)
                                   for square in self.tetromino_object.tetromino]))
        print(current.tolist())
        if self.prev is None:
            self.prev = current
        else:
            print(np.subtract(current, self.prev).tolist())


# Class inherited sprite.Group to handle the Square sprite in each row of play area
class SquareRowGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.movement = False
        self.collision = False
        self.updated_sprites = []
        self.count_sprite_update = 0
        self.num_of_square = 0
