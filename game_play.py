import pygame

from tetromino import Tetromino


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

        self.tetr = Tetromino(self.cell_points_gap, self.square_length, self.first_cell_point)

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.tetr.update(10)
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     print(pygame.mouse.get_pos())
        self.screen.blit(self.bgd_image, (0, 0))
        # self.screen.blit(self.surface, self.play_area_start_point)
        self.tetr.draw(self.screen)
        return 60  # speed
