import pygame
import consts
import random
import game_field

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

def create_night_screen():
    create_grid()
    for i in range(len(game_field.board)):
        for j in range(len(game_field.board[i])):
            if game_field.board[i][j] == "MINE":
                mine = pygame.transform.scale(consts.MINE, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
                window.blit(mine, (j * consts.CELL_SIZE, i * consts.CELL_SIZE))
            if game_field.board[i][j] == "SOLIDER":
                solider = pygame.transform.scale(consts.SOLIDER, (consts.SOLIDER_WIDTH, consts.SOLIDER_HEIGHT))
                window.blit(solider, (j * consts.CELL_SIZE, i * consts.CELL_SIZE))

def create_grid():
    blockSize = 20
    for x in range(0, consts.WINDOW_WIDTH, blockSize):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, "dark green", rect, 1)

window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Adi and Roni")
run = True
create_night_screen()
# create_regular_screen()
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()


