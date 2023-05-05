import pygame
from pygame.locals import K_DOWN


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()
        self.image = pygame.image.load("Resource/block.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

    def update(self):
        self.rect.centery += 10


class Tetris:
    def __init__(self):
        self.speed = 60
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000, 800))
        self.block = [0] * 3
        self.grp1 = pygame.sprite.Group()
        self.grp2 = pygame.sprite.Group()
        for i in range(3):
            self.block[i] = Box((i+1) * 100, 100)
            self.grp1.add(self.block[i])
        self.grp2.add(self.block[1])

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        self.grp1.update()
                        print(self.grp2.sprites())
                        print(self.grp1.sprites())
                        for i in self.grp2.sprites():
                            i.kill()
            self.grp1.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.speed)


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
