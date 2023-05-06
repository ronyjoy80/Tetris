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

    def set_xy(self, x, y, square_group):
        if 0 <= x <= 9 and 0 <= y <= 19:
            self.grid_pos_x = x
            self.grid_pos_y = y
            self.rect.topleft = (self.cell_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                                 self.cell_start_point[1] + self.grid_pos_y * self.cell_points_gap)
        else:
            return True
        if len(pygame.sprite.spritecollide(self, square_group, False)) != 0:
            return True
        return False

    def reverse_update(self, direction):
        if direction == "LEFT":
            self.grid_pos_x += 1
        elif direction == "RIGHT":
            self.grid_pos_x -= 1
        elif direction == "DOWN":
            self.grid_pos_y -= 1
        elif direction == "UP":
            self.grid_pos_y += 1
        self.rect.topleft = (self.cell_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                             self.cell_start_point[1] + self.grid_pos_y * self.cell_points_gap)

    def update(self, direction, group_to_move, square_row_group):
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
            self.rect.topleft = (self.cell_start_point[0] + self.grid_pos_x * self.cell_points_gap,
                                 self.cell_start_point[1] + self.grid_pos_y * self.cell_points_gap)
            group_to_move.updated_sprites.append((self, direction))
            # print(group_to_move.updated_sprites)
            collided_sprites = pygame.sprite.groupcollide(group_to_move, square_row_group, False, False)
            # print(collided_sprites)
            if group_to_move.collision or len(collided_sprites) != 0:
                print("Collision")
                group_to_move.collision = True
                group_to_move.movement = False if direction == "DOWN" else group_to_move.movement
                for square, rev_direction in group_to_move.updated_sprites:
                    square.reverse_update(rev_direction)
        if group_to_move.count_sprite_update == len(group_to_move.sprites()):
            group_to_move.count_sprite_update = 0
            group_to_move.collision = False
            group_to_move.updated_sprites = []


