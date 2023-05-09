import pygame


# Class to design each individual squares in tetrominos
class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_points_gap, square_length, grid_start_point, colors, design):
        super().__init__()
        self.design = design
        self.colors = colors
        self.cell_points_gap = cell_points_gap
        self.grid_start_point = grid_start_point
        self.square_length = square_length

        random_shade = pygame.image.load(("Resource/shade_1.png", "Resource/shade_2.png")[design[1]]).convert_alpha()
        self.shade = pygame.transform.scale(random_shade, (square_length,) * 2)
        self.image = pygame.Surface((square_length,) * 2)
        self.image.fill(self.colors[self.design[0]])
        self.image.blit(self.shade, (0, 0))
        self.rect = self.image.get_rect()
        self.grid_pos_x = x
        self.grid_pos_y = y
        self.rect.topleft = (self.grid_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                             self.grid_start_point[1] + self.grid_pos_y * self.cell_points_gap)

    # update topleft position of the rect
    def update_rect_topleft(self):
        self.rect.topleft = (self.grid_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                             self.grid_start_point[1] + self.grid_pos_y * self.cell_points_gap)

    # update topleft position of the rect using play area grid system
    def set_xy(self, x, y, square_group):
        if 0 <= x <= 9 and 0 <= y <= 19:
            self.grid_pos_x = x
            self.grid_pos_y = y
            self.rect.topleft = (self.grid_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                                 self.grid_start_point[1] + self.grid_pos_y * self.cell_points_gap)
        else:
            return True
        if len(pygame.sprite.spritecollide(self, square_group, False)) != 0:
            return True
        return False

    # reverse the up, down left, right movement
    def reverse_update(self, direction):
        if direction == "LEFT":
            self.grid_pos_x += 1
        elif direction == "RIGHT":
            self.grid_pos_x -= 1
        elif direction == "DOWN":
            self.grid_pos_y -= 1
        elif direction == "UP":
            self.grid_pos_y += 1
        self.rect.topleft = (self.grid_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                             self.grid_start_point[1] + self.grid_pos_y * self.cell_points_gap)

    # Update the color or the position of each Square and check for collision
    def update(self, direction=None, group_to_move=None, square_row_group=None, colors=None, design=None):
        if direction is not None and group_to_move is not None and square_row_group is not None:
            group_to_move.count_sprite_update += 1
            if not group_to_move.collision:
                if direction == "LEFT":
                    group_to_move.collision = True if self.grid_pos_x == 0 else False
                    self.grid_pos_x -= 1
                elif direction == "RIGHT":
                    group_to_move.collision = True if self.grid_pos_x == 9 else False
                    self.grid_pos_x += 1
                elif direction == "DOWN":
                    group_to_move.collision = True if self.grid_pos_y == 19 else False
                    self.grid_pos_y += 1
                elif direction == "UP":
                    group_to_move.collision = True if self.grid_pos_y == 0 else False
                    self.grid_pos_y -= 1
                self.rect.topleft = (self.grid_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                                     self.grid_start_point[1] + self.grid_pos_y * self.cell_points_gap)
                group_to_move.updated_sprites.append((self, direction))
                # print(group_to_move.updated_sprites)
                collided_sprites = pygame.sprite.groupcollide(group_to_move,
                                                              sum([_.sprites() for _ in square_row_group], []), False,
                                                              False)
                # print(collided_sprites)
                if group_to_move.collision or len(collided_sprites) != 0:
                    # print("Collision")
                    group_to_move.collision = True
                    group_to_move.movement = False if direction == "DOWN" else group_to_move.movement
                    for square, rev_direction in group_to_move.updated_sprites:
                        square.reverse_update(rev_direction)
            if group_to_move.count_sprite_update == len(group_to_move.sprites()):
                group_to_move.count_sprite_update = 0
                group_to_move.collision = False
                group_to_move.updated_sprites = []
        elif colors is not None:
            self.colors = colors
            self.image.fill(self.colors[self.design[0]])
            self.image.blit(self.shade, (0, 0))
        elif design is not None:
            self.design = design
            shade = pygame.image.load(("Resource/shade_1.png", "Resource/shade_2.png")[design[1]]).convert_alpha()
            self.shade = pygame.transform.scale(shade, (self.square_length,) * 2)
            self.image.fill(self.colors[self.design[0]])
            self.image.blit(self.shade, (0, 0))
