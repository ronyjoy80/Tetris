import pygame


# Additional Functions

# Function to create image from text and create rect and initialize topleft of the rect
def draw_text_topleft(text, color, xy, size):
    image = pygame.font.Font("Resource/arcade.ttf", size).render(text, True, color).convert_alpha()
    return image, image.get_rect(topleft=xy)


# Function to create image from text and create rect and initialize center of the rect
def draw_text_center(text, color, screen_width, y, size):
    image = pygame.font.Font("Resource/arcade.ttf", size).render(text, True, color).convert_alpha()
    return image, image.get_rect(center=(screen_width / 2, y))


# function to load a table from file and return it as Dictionary
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


# Function to get the top score from file
def get_top_score():
    f = open("Resource/high_score.txt", 'r')
    return f.readline().strip().split()[-2]
