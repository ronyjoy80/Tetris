import pygame
from pygame.locals import K_DOWN

from end_page import EndPage
from game_play import GamePlay
from utils import draw_text_topleft

WHITE = (255, 255, 255)


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

        self.game_state = "start_page"
        image = pygame.image.load("Resource/start_page.png").convert()
        self.start_page_bdg = pygame.transform.scale(image, self.screen.get_size())
        self.image_press_enter = draw_text_topleft("PRESS ENTER", WHITE, (225, 575), 30)

        self.game_play = GamePlay(self.screen, square_length, square_offset)
        self.score = 0
        self.level = 0

        self.end_page = None

    def start_page(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game_state = "game_play"
        self.screen.blit(self.start_page_bdg, (0, 0))
        self.screen.blit(self.image_press_enter[0], self.image_press_enter[1])

    def game_state_selector(self):
        if self.game_state == "start_page":
            self.speed = 60
            self.start_page()
        elif self.game_state == "game_play":
            self.speed = self.game_play.run()
            if self.game_play.game_over:
                self.score = self.game_play.score
                self.level = self.game_play.level
                self.game_state = "end_page"
                self.end_page = EndPage(self.screen, self.score, self.level)
        elif self.game_state == "end_page":
            self.speed = 60
            self.end_page.run()

    def run(self):
        while True:
            self.game_state_selector()
            pygame.display.flip()
            self.clock.tick(self.speed)


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
