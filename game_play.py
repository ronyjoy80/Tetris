import pygame

from game_statistic import GameStatistic
from tetromino import Tetromino, SquareRowGroup

WHITE = (255, 255, 255)


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
        self.grid_start_point = (self.play_area_start_point[0] + self.square_offset,
                                 self.play_area_start_point[1] + self.square_offset)
        print(self.play_area_size)

        self.pause = False
        self.game_over = False
        # self.surface = pygame.Surface(self.play_area_size)
        # self.surface.fill((0, 255, 0))

        self.tetromino = Tetromino(self.cell_points_gap, self.square_length, self.grid_start_point)
        self.next_tetromino = Tetromino(self.cell_points_gap, self.square_length, self.grid_start_point)
        self.square_row_group = [SquareRowGroup() for _ in range(20)]
        self.tetromino_count = {"Z": 0, "O": 0, "I": 0, "J": 0, "L": 0, "S": 0, "T": 0}
        self.game_statistic = GameStatistic(self.screen,
                                            cell_points_gap=self.cell_points_gap,
                                            square_length=self.square_length,
                                            point_statistic=(60, 245),
                                            point_first_tetromino=(80, 320),
                                            tetromino_count=self.tetromino_count,
                                            gap_tetromino=75,
                                            gap_count=120)
        self.image_next_point = (765, 380)
        self.image_next = pygame.font.Font("Resource/arcade.ttf", 23).render("NEXT",
                                                                             True, WHITE).convert_alpha()
        self.next_tetromino_point = (767, 440)
        self.next_tetromino_display = {shape: Tetromino(self.cell_points_gap, self.square_length,
                                                        self.next_tetromino_point, move_to_center=False, shape=shape)
                                       for shape in ["Z", "J", "L", "S", "T"]}
        self.next_tetromino_display["O"] = Tetromino(self.cell_points_gap, self.square_length,
                                                     (782, 440), move_to_center=False, shape="O")
        self.next_tetromino_display["I"] = Tetromino(self.cell_points_gap, self.square_length,
                                                     (751, 440), move_to_center=False, shape="I")

    def tetromino_to_square_row_group(self):
        for sprite in self.tetromino.sprites():
            self.square_row_group[sprite.grid_pos_y].add(sprite)
            self.square_row_group[sprite.grid_pos_y].num_of_square += 1
        count = 0
        for row in range(20):
            if self.square_row_group[row].num_of_square == 10:
                count += 1
                for sprite in self.square_row_group[row].sprites():
                    sprite.kill()
                for group in self.square_row_group[:row]:
                    group.update("DOWN", group, self.square_row_group[row])
                del self.square_row_group[row]
                self.square_row_group = [SquareRowGroup()] + self.square_row_group
        self.tetromino.empty()

    def new_tetromino(self):
        if not self.tetromino.movement:
            self.tetromino_count[self.tetromino.tetromino_object.shape] += 1
            self.tetromino_to_square_row_group()
            self.tetromino = self.next_tetromino
            # noinspection PyTypeChecker
            self.next_tetromino = Tetromino(self.cell_points_gap, self.square_length, self.grid_start_point,
                                            sprites=sum([_.sprites() for _ in self.square_row_group], []))
            # print(self.next_tetromino.failed_to_place)
            if self.next_tetromino.failed_to_place:
                self.game_over = True

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # print(event.key)
                if event.key == pygame.K_DOWN:
                    self.tetromino.update("DOWN", self.tetromino, self.square_row_group)
                    self.new_tetromino()
                elif event.key == pygame.K_LEFT:
                    self.tetromino.update("LEFT", self.tetromino, self.square_row_group)
                elif event.key == pygame.K_RIGHT:
                    self.tetromino.update("RIGHT", self.tetromino, self.square_row_group)
                elif event.key == pygame.K_UP:
                    self.tetromino.update("UP", self.tetromino, SquareRowGroup())
                elif event.key == pygame.K_r:
                    self.tetromino.rotate(sum([_.sprites() for _ in self.square_row_group], []))
                elif event.key == pygame.K_t:
                    self.tetromino.check()
                elif event.key == pygame.K_p:
                    self.pause = not self.pause
                elif event.key in [pygame.K_i, pygame.K_o, pygame.K_j, pygame.K_l, pygame.K_z, pygame.K_s, pygame.K_t]:
                    # noinspection PyTypeChecker
                    self.next_tetromino = Tetromino(self.cell_points_gap, self.square_length, self.grid_start_point,
                                                    sprites=sum([_.sprites() for _ in self.square_row_group], []),
                                                    shape=chr(event.key).upper())
                if self.next_tetromino.failed_to_place:
                    self.game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

        if not self.pause:
            self.tetromino.update("DOWN", self.tetromino, self.square_row_group)
            self.new_tetromino()
        self.screen.blit(self.bgd_image, (0, 0))
        # self.screen.blit(self.surface, self.play_area_start_point)
        self.tetromino.draw(self.screen)
        for i in range(20):
            self.square_row_group[i].draw(self.screen)
        self.game_statistic.draw_statistic()
        self.screen.blit(self.image_next, self.image_next_point)
        self.next_tetromino_display[self.next_tetromino.get_shape()].draw(self.screen)
        return 8  # speed
