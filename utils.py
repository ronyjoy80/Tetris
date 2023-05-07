import pygame


def draw_text_topleft(text, color, xy, size):
    image = pygame.font.Font("Resource/arcade.ttf", size).render(text, True, color).convert_alpha()
    return image, image.get_rect(topleft=xy)


def draw_text_center(text, color, screen_width, y, size):
    image = pygame.font.Font("Resource/arcade.ttf", size).render(text, True, color).convert_alpha()
    return image, image.get_rect(center=(screen_width / 2, y))


def load_table(file):
    f = open(file, 'r')
    table = {}
    while True:
        table_line = f.readline()
        if table_line == '':
            break
        else:
            c = table_line.strip().split()
            table[int(c[0])] = int(c[1])
    f.close()
    return table


def get_top_score():
    f = open("Resource/high_score.txt", 'r')
    return f.readline().strip().split()[-2]

