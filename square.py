import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Resource/square.jpg")
        self.rect = self.image.get_rect()
        self.color = (255, 255, 255)
