import pygame

from utils import draw_text_center, draw_text_topleft

WHITE = (255, 255, 255)
RED = (255, 0, 0)


# Class to display the last Page
class EndPage:
    def __init__(self, screen, score, level):
        self.screen = screen
        screen_w = self.screen.get_width()

        self.high_score = {}
        self.get_high_score()
        self.rank = False
        self.image_msg = []
        self.name = ""
        self.name_length = 0
        self.image_name = draw_text_center("", WHITE, screen_w, 430, 35)
        self.restart = False

        for i in range(1, 4):
            if score > int(self.high_score[i][1]):
                self.rank = i
                break
        if self.rank:
            for rank in range(3, self.rank, -1):
                self.high_score[rank] = self.high_score[rank - 1]
            self.high_score[self.rank] = ["YOU", f"{score:06}", f"{level:02}"]
            self.image_msg = [draw_text_center("CONGRATULATIONS", RED, screen_w, 200, 27),
                              draw_text_center("YOU ARE A TETRIS MASTER.", WHITE, screen_w, 250, 27),
                              draw_text_center("PLEASE ENTER YOUR NAME", WHITE, screen_w, 300, 27),
                              draw_text_center("AND PRESS ENTER TO RESTART", WHITE, screen_w, 350, 27)]
        else:
            self.image_msg = [draw_text_center("BETTER", WHITE, screen_w, 250, 27),
                              draw_text_center("LUCK", RED, screen_w, 300, 27),
                              draw_text_center("NEXT TIME", WHITE, screen_w, 350, 27),
                              draw_text_center("PRESS ENTER TO RESTART", WHITE, screen_w, 410, 27)]

        image = pygame.image.load("Resource/end_page.png").convert()
        self.bgd_image = pygame.transform.scale(image, self.screen.get_size())
        self.image_high_score = [draw_text_center("HIGH SCORE", WHITE, screen_w, 75, 27),
                                 draw_text_center("   NAME    SCORE    LV", WHITE, screen_w, 540, 27)]
        rank_start_x, rank_start_y = 200, 600
        rank_gap_y = 50
        rank_gap_x = [80, 300, 542]
        for rank in range(1, 4):
            y = rank_start_y + (rank - 1) * rank_gap_y
            self.image_high_score.append(draw_text_topleft(str(rank), WHITE, (rank_start_x, y), 27))
            for i in range(3):
                self.image_high_score.append(draw_text_topleft(self.high_score[rank][i], WHITE,
                                                               (rank_start_x + rank_gap_x[i], y), 27))
        # print(self.image_high_score)

    # function to retrieve high score information from  file "high_score.txt"
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

    # function to write high score information from  file "high_score.txt"
    def write_to_file(self):
        f = open("Resource/high_score.txt", 'w')
        for rank in range(1, 4):
            f.write(f"{rank}\t{self.high_score[rank][0]}\t{self.high_score[rank][1]}\t{self.high_score[rank][2]}\n")
        f.close()

    # function to blit image with rect
    def blit_rect(self, image):
        self.screen.blit(image[0], image[1])

    # event loop of the end page
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_RETURN:
                    if self.rank:
                        if self.name != "":
                            self.high_score[self.rank][0] = self.name
                        else:
                            self.high_score[self.rank] = "------"
                        self.write_to_file()
                    self.restart = True
                elif len(self.name) <= 5 and self.rank and pygame.K_a <= event.key <= pygame.K_z:
                    self.name += chr(event.key - 32 if event.mod & pygame.KMOD_SHIFT else event.key)
                    self.image_name = draw_text_center(self.name,  WHITE,
                                                       self.image_name[1].centerx * 2, self.image_name[1].centery, 35)

        self.screen.blit(self.bgd_image, (0, 0))
        self.blit_rect(self.image_name)
        for image in self.image_high_score:
            self.blit_rect(image)
        for msg in self.image_msg:
            self.blit_rect(msg)
