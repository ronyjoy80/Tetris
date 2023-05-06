import pygame

from tetromino import Tetromino, SquareRowGroup


class GamePlay:
    def __init__(self, screen, square_length, square_offset):
        self.screen = screen
        self.square_length = square_length
        self.square_offset = square_offset
        self.cell_points_gap = self.square_length + self.square_offset
        image = pygame.image.load("Resource/gameplay_background.png").convert()
        self.bgd_image = pygame.transform.scale(image, self.screen.get_size())
        self.bgd_width, self.bgd_height = self.bgd_image.get_size()
        self.play_area_start_point = (self.bgd_width * 0.375, self.bgd_height * 0.183)
        self.play_area_width = self.bgd_width * 0.686 - self.play_area_start_point[0]
        self.play_area_height = self.bgd_height * 0.894 - self.play_area_start_point[1]
        self.play_area_size = (self.play_area_width, self.play_area_height)
        self.first_cell_point = (self.play_area_start_point[0] + self.square_offset,
                                 self.play_area_start_point[1] + self.square_offset)
        print(self.play_area_size)

        # self.surface = pygame.Surface(self.play_area_size)
        # self.surface.fill((0, 255, 0))

        self.tetromino = Tetromino(self.cell_points_gap, self.square_length, self.first_cell_point)
        self.square_row_group = [SquareRowGroup() for _ in range(20)]

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.tetromino.update("DOWN", self.tetromino, sum([_.sprites() for _ in self.square_row_group], []))
                elif event.key == pygame.K_LEFT:
                    self.tetromino.update("LEFT", self.tetromino, sum([_.sprites() for _ in self.square_row_group], []))
                elif event.key == pygame.K_RIGHT:
                    self.tetromino.update("RIGHT", self.tetromino,
                                          sum([_.sprites() for _ in self.square_row_group], []))
                elif event.key == pygame.K_UP:
                    self.tetromino.update("UP", self.tetromino, SquareRowGroup())
                elif event.key == pygame.K_r:
                    self.tetromino.rotate()
                elif event.key == pygame.K_t:
                    self.tetromino.check()
        if not self.tetromino.movement:
            for sprite in self.tetromino.sprites():
                self.square_row_group[sprite.grid_pos_y].add(sprite)
                self.square_row_group[sprite.grid_pos_y].num_of_square += 1
            count = 0
            for row in range(20):
                if self.square_row_group[row].num_of_square == 10:
                    for sprite in self.square_row_group[row].sprites():
                        sprite.kill()
                    for group in self.square_row_group[:row]:
                        group.update("DOWN", group, self.square_row_group[row])
                    del self.square_row_group[row]
                    self.square_row_group = [SquareRowGroup()] + self.square_row_group
            self.tetromino.empty()
            self.tetromino = Tetromino(self.cell_points_gap, self.square_length, self.first_cell_point)
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     print(pygame.mouse.get_pos())
        self.screen.blit(self.bgd_image, (0, 0))
        # self.screen.blit(self.surface, self.play_area_start_point)
        self.tetromino.draw(self.screen)
        for i in range(20):
            self.square_row_group[i].draw(self.screen)
        return 120  # speed
