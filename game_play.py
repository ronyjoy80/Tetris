import pygame

from game_statistic import GameStatistic
from tetromino import Tetromino, SquareRowGroup
from utils import draw_text_topleft, load_table, get_top_score

WHITE = (255, 255, 255)


class GamePlay:
    def __init__(self, screen, square_length, square_offset):
        self.cheat = False
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
        self.score = 0
        self.points = [0, 40, 100, 300, 1200]
        self.level = 0
        self.prev_level_lines = 0
        self.lines = 0
        self.level_speed = load_table("Resource/level_speed.txt")
        self.cycle_time = 60
        self.speed = self.cycle_time / self.level_speed[self.level]
        self.level_change = load_table("Resource/level_change.txt")
        self.colors = [((230, 25, 75), (60, 180, 75)),
                       ((255, 225, 25), (0, 130, 200)),
                       ((245, 130, 48), (145, 30, 180)),
                       ((70, 240, 240), (240, 50, 230)),
                       ((210, 245, 60), (250, 190, 212)),
                       ((0, 128, 128), (220, 190, 255)),
                       ((170, 110, 40), (255, 250, 200)),
                       ((128, 0, 0), (170, 255, 195)),
                       ((128, 128, 0), (255, 215, 180)),
                       ((0, 0, 128), (128, 128, 128))]
        self.color = self.colors[0]
        # self.surface = pygame.Surface(self.play_area_size)
        # self.surface.fill((0, 255, 0))

        self.tetromino = Tetromino(self.cell_points_gap, self.square_length, self.grid_start_point, self.color)
        self.next_tetromino = Tetromino(self.cell_points_gap, self.square_length, self.grid_start_point, self.color)
        self.square_row_group = [SquareRowGroup() for _ in range(20)]
        self.tetromino_count = {"Z": 0, "O": 0, "I": 0, "J": 0, "L": 0, "S": 0, "T": 0}
        self.game_statistic = GameStatistic(self.screen,
                                            cell_points_gap=self.cell_points_gap,
                                            square_length=self.square_length,
                                            point_statistic=(60, 245),
                                            point_first_tetromino=(80, 320),
                                            tetromino_count=self.tetromino_count,
                                            gap_tetromino=75,
                                            gap_count=120,
                                            color=self.color)

        self.image_next = draw_text_topleft("NEXT", WHITE, (750, 380), 30)
        self.next_tetromino_point = (767, 440)
        self.next_tetromino_display = {shape: Tetromino(self.cell_points_gap, self.square_length,
                                                        self.next_tetromino_point, self.color,
                                                        move_to_center=False, shape=shape)
                                       for shape in ["Z", "J", "L", "S", "T"]}
        self.next_tetromino_display["O"] = Tetromino(self.cell_points_gap, self.square_length,
                                                     (782, 440), self.color, move_to_center=False, shape="O")
        self.next_tetromino_display["I"] = Tetromino(self.cell_points_gap, self.square_length,
                                                     (751, 440), self.color, move_to_center=False, shape="I")

        self.image_lines = draw_text_topleft("LINES-", WHITE, (380, 60), 30)
        self.image_lines_count = draw_text_topleft(f"{self.lines:03}", WHITE, (580, 60), 30)

        self.image_game_mode = draw_text_topleft("SINGLE", WHITE, (113, 93), 25)

        score_board_x, score_board_y = 750, 80
        self.image_top_score = draw_text_topleft("TOP", WHITE, (score_board_x, score_board_y), 30)
        self.image_top_score_val = draw_text_topleft(get_top_score(), WHITE, (score_board_x, score_board_y + 40), 30)
        self.image_score = draw_text_topleft("SCORE", WHITE, (score_board_x, score_board_y + 110), 30)
        self.image_score_val = draw_text_topleft("000000", WHITE, (score_board_x, score_board_y + 150), 30)

        level_x, level_y = 750, 586
        self.image_level = draw_text_topleft("LEVEL", WHITE, (level_x, level_y), 27)
        self.image_level_val = draw_text_topleft("00", WHITE, (level_x + 55, level_y + 40), 27)

    # Function to increment the level
    def level_inc(self):
        self.level += 1
        self.image_level_val = draw_text_topleft(f"{self.level:02}", WHITE, self.image_level_val[1].topleft, 27)
        self.color = self.colors[self.level % 10]
        self.tetromino.update(colors=self.color)
        self.next_tetromino.update(colors=self.color)
        for group in self.square_row_group:
            group.update(colors=self.color)
        for group in self.game_statistic.tetromino:
            group.update(colors=self.color)
        for shape in ["Z", "J", "L", "S", "T", "I", "O"]:
            self.next_tetromino_display[shape].update(colors=self.color)
        if self.level < 30:
            self.speed = self.cycle_time / self.level_speed[self.level]
        else:
            self.speed = self.cycle_time

    # Function to transfer sprites from "Tetromino" to "SquareRowGroup" object and calculate scores, level up, lines
    def tetromino_to_square_row_group(self):
        for sprite in self.tetromino.sprites():
            self.square_row_group[sprite.grid_pos_y].add(sprite)
            self.square_row_group[sprite.grid_pos_y].num_of_square += 1
        count = 0
        prev_score = self.score
        for row in range(20):
            if self.square_row_group[row].num_of_square == 10:
                count += 1
                for sprite in self.square_row_group[row].sprites():
                    sprite.kill()
                for group in self.square_row_group[:row]:
                    group.update("DOWN", group, self.square_row_group[row])
                del self.square_row_group[row]
                self.square_row_group = [SquareRowGroup()] + self.square_row_group
        self.score += (self.level + 1) * self.points[count]
        self.lines += count
        if self.level < 26:
            if self.level_change[self.level] < self.lines - self.prev_level_lines:
                self.prev_level_lines += self.level_change[self.level]
                self.level_inc()
        else:
            if 200 < self.lines - self.prev_level_lines:
                self.prev_level_lines += 200
                self.level_inc()
        if prev_score != self.score:
            self.image_score_val = draw_text_topleft(f"{self.score:06}", WHITE, self.image_score_val[1].topleft, 30)
            self.image_lines_count = draw_text_topleft(f"{self.lines:03}", WHITE, self.image_lines_count[1].topleft, 30)
        self.tetromino.empty()

    # Creating new tetromino after current tetromino movement stops
    def new_tetromino(self):
        if not self.tetromino.movement:
            self.tetromino_count[self.tetromino.tetromino_object.shape] += 1
            self.tetromino_to_square_row_group()
            self.tetromino = self.next_tetromino
            # noinspection PyTypeChecker
            self.next_tetromino = Tetromino(self.cell_points_gap, self.square_length, self.grid_start_point, self.color,
                                            sprites=sum([_.sprites() for _ in self.square_row_group], []))
            self.next_tetromino_display[self.next_tetromino.get_shape()].update(design=self.next_tetromino.get_design())
            # print(self.next_tetromino.failed_to_place)
            if self.next_tetromino.failed_to_place:
                self.game_over = True

    # function to blit an image using rect of the image to the screen
    def blit_rect(self, image):
        self.screen.blit(image[0], image[1])

    # event loop of game play
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # print(event.key)
                if event.key == pygame.K_DOWN:
                    # move tetromino Down
                    self.tetromino.update("DOWN", self.tetromino, self.square_row_group)
                    self.new_tetromino()
                    self.speed = 60
                elif event.key == pygame.K_LEFT:
                    # move tetromino Left
                    self.tetromino.update("LEFT", self.tetromino, self.square_row_group)
                elif event.key == pygame.K_RIGHT:
                    # move tetromino Right
                    self.tetromino.update("RIGHT", self.tetromino, self.square_row_group)
                elif event.key == pygame.K_UP and self.cheat:
                    # move tetromino up
                    self.tetromino.update("UP", self.tetromino, SquareRowGroup())
                elif event.key == pygame.K_q:
                    self.tetromino.rotate(sum([_.sprites() for _ in self.square_row_group], []), 1)
                elif event.key == pygame.K_e:
                    self.tetromino.rotate(sum([_.sprites() for _ in self.square_row_group], []), -1)
                elif event.key == pygame.K_h and self.cheat:
                    self.tetromino.check()
                elif event.key == pygame.K_p and self.cheat:
                    self.pause = not self.pause
                elif event.key == pygame.K_g and self.cheat:
                    self.game_over = True
                elif event.key == pygame.K_c and self.cheat:
                    self.level_inc()
                elif event.key == pygame.K_x and event.mod & pygame.KMOD_SHIFT and event.mod & pygame.KMOD_CTRL:
                    self.cheat = not self.cheat
                elif event.key in [pygame.K_i, pygame.K_o, pygame.K_j, pygame.K_l, pygame.K_z, pygame.K_s, pygame.K_t]:
                    if self.cheat:
                        # noinspection PyTypeChecker
                        self.next_tetromino = Tetromino(self.cell_points_gap, self.square_length, self.grid_start_point,
                                                        self.color,
                                                        sprites=sum([_.sprites() for _ in self.square_row_group], []),
                                                        shape=chr(event.key).upper())
                if self.next_tetromino.failed_to_place:
                    self.game_over = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    if self.level < 30:
                        self.speed = self.cycle_time / self.level_speed[self.level]
                    else:
                        self.speed = self.cycle_time
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
        self.blit_rect(self.image_next)
        self.next_tetromino_display[self.next_tetromino.get_shape()].draw(self.screen)

        self.blit_rect(self.image_lines)
        self.blit_rect(self.image_lines_count)
        self.blit_rect(self.image_game_mode)

        self.blit_rect(self.image_top_score)
        self.blit_rect(self.image_top_score_val)
        self.blit_rect(self.image_score)
        self.blit_rect(self.image_score_val)

        self.blit_rect(self.image_level)
        self.blit_rect(self.image_level_val)

        return self.speed
