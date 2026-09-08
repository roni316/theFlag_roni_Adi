import consts
import random

from consts import *


def initialize_board():
    global board

    board =  [[EMPTY_BOX for col in range(consts.BOARD_COLS)] for row in
            range(consts.BOARD_ROWS)]


def random_mines():
    for i in range(consts.MINES_COUNT):
        x = random.randrange(consts.BOARD_ROWS)
        y = random.randrange(consts.BOARD_COLS)
        while board[x][y] != EMPTY_BOX:
            x = random.randrange(consts.BOARD_ROWS)
            y = random.randrange(consts.BOARD_COLS)
        board[x][y] = MINE_BOX
    return board

def init_flag():
    for i in range(consts.BOARD_ROWS - consts.FLAG_ROWS , consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS - consts.FLAG_COLS , consts.BOARD_COLS):
            board[i][j] = FLAG_BOX

    return board




initialize_board()