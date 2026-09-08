import consts
import random

def initialize_board():
    global board

    board =  [["EMPTY" for col in range(consts.BOARD_COLS)] for row in
            range(consts.BOARD_ROWS)]
    return board


def random_mines(board):
    for i in range(consts.MINES_COUNT):
        x = random.randrange(consts.BOARD_ROWS)
        y = random.randrange(consts.BOARD_COLS)
        while board[x][y] != "EMPTY":
            x = random.randrange(consts.BOARD_ROWS)
            y = random.randrange(consts.BOARD_COLS)
        board[x][y] = "MINE"
    print(board)

board = initialize_board()
random_mines(board)
