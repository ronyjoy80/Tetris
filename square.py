import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_points_gap, square_length, cell_start_point):
        super().__init__()
        self.cell_points_gap = cell_points_gap
        self.cell_start_point = cell_start_point
        self.image = pygame.transform.scale(pygame.image.load("Resource/square.jpg"), (square_length,) * 2)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.color = (255, 255, 255)
        self.grid_pos_x = x
        self.grid_pos_y = y
        self.rect.topleft = (self.cell_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                             self.cell_start_point[1] + self.grid_pos_y * self.cell_points_gap)

    def update(self, check):
        self.grid_pos_x += 1
        self.grid_pos_y += 1
        self.rect.topleft = (self.cell_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                             self.cell_start_point[1] + self.grid_pos_y * self.cell_points_gap)
