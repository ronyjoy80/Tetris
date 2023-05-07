import pygame
from pygame.locals import K_DOWN

from game_play import GamePlay


class Tetris:
    def __init__(self):
        square_offset = 1
        square_length = 30
        play_area_w, play_area_l = square_length * 10 + square_offset * 11, square_length * 20 + square_offset * 21
        bgd_image_w, bgd_image_l = pygame.image.load("Resource/gameplay_background.png").get_size()
        screen_size = ((play_area_w * bgd_image_w) / 318.3, (play_area_l * bgd_image_l) / 548.4)
        print(screen_size)
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Tetris")
        pygame.display.set_icon(pygame.image.load("Resource/icon.png").convert_alpha())
        self.speed = 60
        self.clock = pygame.time.Clock()
        self.game_state = "game_play"
        self.game_play = GamePlay(self.screen, square_length, square_offset)

    def game_state_selector(self):
        if self.game_state == "game_play":
            self.speed = self.game_play.run()
            if self.game_play.game_over:
                self.game_state = "end_page"

    def run(self):
        while True:
            self.game_state_selector()
            pygame.display.flip()
            self.clock.tick(self.speed)


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
