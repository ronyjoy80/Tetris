import pygame.font

from tetromino import Tetromino
from utils import draw_text_topleft

WHITE = (255, 255, 255)


class GameStatistic:
    def __init__(self, screen, **kwargs):
        self.screen = screen
        cell_points_gap = kwargs["cell_points_gap"]
        square_length = kwargs["square_length"]
        point_first_tetromino = list(kwargs["point_first_tetromino"])
        gap_tetromino = kwargs["gap_tetromino"]
        color = kwargs["color"]
        self.gap_count = kwargs["gap_count"]
        self.tetromino_count = kwargs["tetromino_count"]
        self.image_statistic = draw_text_topleft("STATISTIC", WHITE, kwargs["point_statistic"], 27)
        self.tetromino = []
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), color, move_to_center=False, shape="T"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), color, move_to_center=False, shape="J"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), color, move_to_center=False, shape="Z"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), color, move_to_center=False, shape="O"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), color, move_to_center=False, shape="S"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), color, move_to_center=False, shape="L"))

    def draw_statistic(self):
        self.screen.blit(self.image_statistic[0], self.image_statistic[1])
        for tetromino in self.tetromino:
            tetromino.draw(self.screen)
            num_image = draw_text_topleft(str(self.tetromino_count[tetromino.get_shape()]), WHITE,
                                          (tetromino.grid_start_point[0] + self.gap_count,
                                           tetromino.grid_start_point[1]), 30)
            self.screen.blit(num_image[0], num_image[1])
