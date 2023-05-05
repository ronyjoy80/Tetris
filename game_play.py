import pygame


class GamePlay:
    def __init__(self, screen):
        self.screen = screen
        self.bgd_image = pygame.image.load("Resource/gameplay_background.png").convert()
        self.bgd_width, self.bgd_height = self.bgd_image.get_size()
        self.play_area_start_point = (self.bgd_width * 0.375, self.bgd_height * 0.182)
        self.play_area_width = self.bgd_width * 0.686 - self.play_area_start_point[0]
        self.play_area_height = self.bgd_height * 0.894 - self.play_area_start_point[1]
        self.play_area_size = (self.play_area_width, self.play_area_height)

        self.surface = pygame.Surface(self.play_area_size)
        self.surface.fill((0, 255, 0))

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     print(pygame.mouse.get_pos())
        self.screen.blit(self.bgd_image, (0, 0))
        self.screen.blit(self.surface, self.play_area_start_point)
        return 60  # speed
