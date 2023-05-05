import pygame
from pygame.locals import K_DOWN

from game_play import GamePlay


class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode(pygame.image.load("Resource/gameplay_background.png").get_size())
        pygame.display.set_caption("Tetris")
        pygame.display.set_icon(pygame.image.load("Resource/icon.png").convert_alpha())
        self.speed = 60
        self.clock = pygame.time.Clock()
        self.game_state = "game_play"
        self.game_play = GamePlay(self.screen)

    def game_state_selector(self):
        if self.game_state == "game_play":
            self.speed = self.game_play.run()

    def run(self):
        while True:
            self.game_state_selector()
            pygame.display.flip()
            self.clock.tick(self.speed)


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
