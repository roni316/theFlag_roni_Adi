import consts
import random

from consts import *

#initialized empty board
def initialize_board():
    global board
    board =  [[EMPTY_BOX for col in range(consts.BOARD_COLS)] for row in
            range(consts.BOARD_ROWS)]

#inserts mines into random places
def random_mines():
    for i in range(consts.MINES_COUNT):
        x = random.randrange(consts.BOARD_ROWS)
        y = random.randrange(consts.BOARD_COLS)
        while board[x][y] != EMPTY_BOX:
            x = random.randrange(consts.BOARD_ROWS)
            y = random.randrange(consts.BOARD_COLS)
        board[x][y] = MINE_BOX
    return board

#initiates flag
def init_flag():
    for i in range(consts.BOARD_ROWS - consts.FLAG_ROWS , consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS - consts.FLAG_COLS , consts.BOARD_COLS):
            board[i][j] = FLAG_BOX

    return board

#initiates soldier
def init_soldier():
    for i in range(SOLDIER_BODY_ROWS):
        for j in range(SOLDIER_COLS):
            board[i][j] = SOLIDER_BODY_BOX

    for i in range(SOLDIER_BODY_ROWS, (SOLDIER_BODY_ROWS + SOLDIER_FEET_ROWS)):
        for j in range(SOLDIER_COLS):
            board[i][j] = SOLIDER_FEET_BOX


def final_board():
    initialize_board()
    random_mines()
    init_flag()
    init_soldier()
    return board


board = final_board()
for i in board:
    print(i)