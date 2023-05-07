import pygame

from utils import draw_text_center, draw_text_topleft

WHITE = (255, 255, 255)
RED = (255, 0, 0)


class EndPage:
    def __init__(self, screen, score, level):
        self.screen = screen
        screen_w = self.screen.get_width()

        self.high_score = {}
        self.get_high_score()
        self.rank = 1
        self.image_msg = []

        for i in range(1, 4):
            if score > int(self.high_score[i][1]):
                self.rank = i
                break
        if self.rank:
            for rank in range(3, self.rank, -1):
                self.high_score[rank] = self.high_score[rank - 1]
            self.high_score[self.rank] = ["YOU", str(score), str(level)]
            self.image_msg = [draw_text_center("CONGRATULATIONS", RED, screen_w, 200, 27),
                              draw_text_center("YOU ARE A TETRIS MASTER.", WHITE, screen_w, 250, 27),
                              draw_text_center("PLEASE ENTER YOUR NAME", WHITE, screen_w, 300, 27),
                              draw_text_center("AND PRESS ENTER", WHITE, screen_w, 350, 27)]
        else:
            self.image_msg = [draw_text_center("BETTER", WHITE, screen_w, 250, 27),
                              draw_text_center("LUCK", RED, screen_w, 300, 27),
                              draw_text_center("NEXT TIME", WHITE, screen_w, 350, 27)]

        image = pygame.image.load("Resource/end_page.png").convert()
        self.bgd_image = pygame.transform.scale(image, self.screen.get_size())
        self.image_high_score = [draw_text_center("HIGH SCORE", WHITE, screen_w, 75, 27),
                                 draw_text_center("RANK NAME   SCORE    LV", WHITE, screen_w, 540, 27)]
        rank_start_x, rank_start_y = 100, 600
        rank_gap_x, rank_gap_y = 100, 100
        # for rank in range(1, 4):
        #     for i in range(3):


    def get_high_score(self):
        f = open("Resource/high_score.txt", 'r')
        while True:
            line = f.readline()
            if line == '':
                break
            else:
                c = line.strip().split()
                self.high_score[int(c[0])] = c[1:]
        f.close()

    def blit_rect(self, image):
        self.screen.blit(image[0], image[1])

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.screen.blit(self.bgd_image, (0, 0))
        self.blit_rect(self.image_high_score)
        self.blit_rect(self.image_table_label)
        for msg in self.image_msg:
            self.blit_rect(msg)
