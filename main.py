import pygame
from pygame.locals import K_DOWN

from end_page import EndPage
from game_play import GamePlay
from utils import draw_text_topleft

WHITE = (255, 255, 255)


# Documentation guide:
#       blit = Draw an image on to a surface
#       rect = create a rectangle around an image and store that dimensions
#
# Game Controls:
#       Movement of tetromino   = left, down, right arrow key
#       Rotate tetromino        = R
#   Cheat Keys: press crt + shift + x to goto cheat mode
#       Move tetromino to up    = up arrow key
#       Pause                   = p
#       Game Over               = g
#       Level Increment         = c
#       Print Tetromino Pos     = h
#       Press corresponding shape letter to set next Tetromino

# Class "Tetris" defines entire game Tetris
class Tetris:
    def __init__(self):
        self.square_offset = 1
        self.square_length = 30
        play_area_w = self.square_length * 10 + self.square_offset * 11
        play_area_l = self.square_length * 20 + self.square_offset * 21
        bgd_image_w, bgd_image_l = pygame.image.load("Resource/gameplay_background.png").get_size()
        screen_size = ((play_area_w * bgd_image_w) / 318.3, (play_area_l * bgd_image_l) / 548.4)
        print(screen_size)
        # Initialize all imported pygame modules
        pygame.init()
        # Initialize a window or screen for display
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Tetris")
        pygame.display.set_icon(pygame.image.load("Resource/icon.png").convert_alpha())
        self.speed = 60
        # Creating  an object of "pygame.time.Clock" to help track time
        self.clock = pygame.time.Clock()

        # Initialize game state to intro page
        self.game_state = "start_page"
        # Load image from file and convert to the same pixel format  fo screen which makes bliting faster
        image = pygame.image.load("Resource/start_page.png").convert()
        # scaling the image
        self.start_page_bdg = pygame.transform.scale(image, self.screen.get_size())
        # creating an image from text
        self.image_press_enter = draw_text_topleft("PRESS ENTER", WHITE, (225, 575), 30)

        self.game_play = None
        self.score = 0
        self.level = 0

        self.end_page = None

    # Function to display intro page of the game
    def start_page(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game_state = "game_play"
                    self.game_play = GamePlay(self.screen, self.square_length, self.square_offset)
        self.screen.blit(self.start_page_bdg, (0, 0))
        self.screen.blit(self.image_press_enter[0], self.image_press_enter[1])

    # function to select which page to display
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
            if self.end_page.restart:
                self.game_state = "start_page"

    # Game Loop
    def run(self):
        while True:
            self.game_state_selector()
            # update the screen so that changes will be shown
            pygame.display.flip()
            # clock.tock() manages no of frames per second
            self.clock.tick(self.speed)


if __name__ == '__main__':
    tetris = Tetris()
    tetris.run()
