import pygame
import consts
import random

def create_regular_screen():
    window.fill(consts.BACKGROUND_COLOR)
    solider = pygame.transform.scale(consts.SOLIDER, (consts.SOLIDER_WIDTH, consts.SOLIDER_HEIGHT))
    window.blit(solider,(0,0))
    flag = pygame.transform.scale(consts.FLAG, (consts.FLAG_WIDTH, consts.FLAG_HEIGHT))
    window.blit(flag,( consts.FLAG_COL_DES * consts.CELL_SIZE, consts.FLAG_ROW_DES * consts.CELL_SIZE))
    grass = pygame.transform.scale(consts.GRASS, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    destination = get_random_location()
    for i in range(consts.MINES_COUNT):
        window.blit(grass,(destination[i][1] * consts.CELL_SIZE, destination[i][0] * consts.CELL_SIZE))

def get_random_location():
    location_list = []
    row = random.sample(range(1,consts.BOARD_ROWS-1), consts.MINES_COUNT)
    col = random.sample(range(1,consts.BOARD_COLS-3), consts.MINES_COUNT)
    for i in range(len(row)):
        add = (row[i], col[i])
        location_list.append(add)
    return location_list
pygame.init()

window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Adi and Roni")
run = True
create_regular_screen()
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()


