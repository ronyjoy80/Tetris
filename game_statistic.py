import pygame.font

from tetromino import Tetromino

WHITE = (255, 255, 255)


class GameStatistic:
    def __init__(self, screen, **kwargs):
        self.screen = screen
        cell_points_gap = kwargs["cell_points_gap"]
        square_length = kwargs["square_length"]
        point_first_tetromino = list(kwargs["point_first_tetromino"])
        gap_tetromino = kwargs["gap_tetromino"]
        self.gap_count = kwargs["gap_count"]
        self.point_statistic = kwargs["point_statistic"]
        self.tetromino_count = kwargs["tetromino_count"]
        self.image_statistic = pygame.font.Font("Resource/arcade.ttf", 23).render("STATISTICS",
                                                                                  True, WHITE).convert_alpha()
        self.tetromino = []
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), move_to_center=False, shape="T"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), move_to_center=False, shape="J"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), move_to_center=False, shape="Z"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), move_to_center=False, shape="O"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), move_to_center=False, shape="S"))
        point_first_tetromino[1] += gap_tetromino
        self.tetromino.append(Tetromino(cell_points_gap, square_length,
                                        tuple(point_first_tetromino), move_to_center=False, shape="L"))

    def draw_statistic(self):
        self.screen.blit(self.image_statistic, self.point_statistic)
        for tetromino in self.tetromino:
            tetromino.draw(self.screen)

            self.screen.blit(
                pygame.font.Font("Resource/arcade.ttf", 23).render(str(self.tetromino_count[tetromino.get_shape()]),
                                                                   True, WHITE).convert_alpha(),
                (tetromino.grid_start_point[0] + self.gap_count, tetromino.grid_start_point[1]))
