import clock
import pygame
from fontTools.tfmLib import PASSTHROUGH

import consts
import random
import game_field
import soldier
import main
import time




def lose():
    quit()



def win():
    pass


def find_solider_location():
    print(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == consts.SOLIDER_BODY_BOX:
                des = (i,j)
                return des
    return None

def create_regular_screen(destination_grass):
    window.fill(consts.BACKGROUND_COLOR)
    solider = pygame.transform.scale(consts.SOLIDER, (consts.SOLIDER_WIDTH, consts.SOLIDER_HEIGHT))
    destination = find_solider_location()
    window.blit(solider,(destination[1] * consts.CELL_SIZE, destination[0] * consts.CELL_SIZE))
    flag = pygame.transform.scale(consts.FLAG, (consts.FLAG_WIDTH, consts.FLAG_HEIGHT))
    window.blit(flag,( consts.FLAG_COL_DES * consts.CELL_SIZE, consts.FLAG_ROW_DES * consts.CELL_SIZE))
    grass = pygame.transform.scale(consts.GRASS, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    for i in range(consts.MINES_COUNT):
        window.blit(grass,(destination_grass[i][1] * consts.CELL_SIZE, destination_grass[i][0] * consts.CELL_SIZE))

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
    window.fill("black")
    create_grid()
    board = game_field.final_board()
    count = 0
    print(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == consts.MINE_BOX:
                mine = pygame.transform.scale(consts.MINE, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
                window.blit(mine, (j * consts.CELL_SIZE, i * consts.CELL_SIZE))
            if board[i][j] == consts.SOLIDER_BODY_BOX and count == 0:
                count = 1
                night_solider = pygame.transform.scale(consts.SOLIDER_NIGHT, (consts.SOLIDER_WIDTH, consts.SOLIDER_HEIGHT))
                destination = find_solider_location()
                window.blit(night_solider, (destination[1] * consts.CELL_SIZE, destination[0] * consts.CELL_SIZE))

def create_grid():
    blockSize = 20
    for x in range(0, consts.WINDOW_WIDTH, blockSize):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, "dark green", rect, 1)

''' the function creates '''
def night_vision(grass_destination):
    run_end = pygame.time.get_ticks() + 1000
    create_night_screen()
    while pygame.time.get_ticks() < run_end:
        pygame.display.flip()
    create_regular_screen(grass_destination)
    pygame.display.flip()

board = game_field.final_board()
window = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Adi and Roni")
run = True
destination = get_random_location()
create_regular_screen(destination)
pygame.display.flip()
count_row = 0
count = 0
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and count == 0:
                night_vision(destination)
                count += 1
            if event.key == pygame.K_DOWN and count_row < consts.BOARD_ROWS - 4:
                count_row += 1
                board = soldier.move_soldier_down(board)
                create_regular_screen(destination)
                pygame.display.flip()
            if event.type == pygame.QUIT:
                run = False
pygame.quit()




