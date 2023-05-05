import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Resource/square.jpg")
        self.rect = self.image.get_rect()
        self.color = (255, 255, 255)
        self.grid_pos_x = x
        self.grid_pos_y = y
