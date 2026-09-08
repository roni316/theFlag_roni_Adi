import consts
import game_field

from consts import *

def init_soldier(board):
    for i in range(SOLDIER_ROWS):
        for j in range(SOLDIER_COLS):
            board[i][j] = SOLIDER_BOX

game_field.initialize_board()
game_field.random_mines()
board = game_field.init_flag()
init_soldier(game_field.board)
for i in range(len(board)):
        print(board[i])


