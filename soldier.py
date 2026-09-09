import game_field

from consts import *


#moves the soldier left in the matrix
def move_soldier_left():
    for row in range(len(game_field.final_board())):
        for col in range(len(game_field.final_board()[row])):
            if game_field.final_board()[row][col] == SOLIDER_BODY_BOX:
                game_field.final_board()[row][col] = EMPTY_BOX
                game_field.final_board()[row][col+1] = SOLIDER_BODY_BOX

    for row in range(len(game_field.final_board())):
        for col in range(len(game_field.final_board()[row])):
            if game_field.final_board()[row][col] == SOLIDER_FEET_BOX:
                game_field.final_board()[row][col] = EMPTY_BOX
                game_field.final_board()[row][col+1] = SOLIDER_FEET_BOX


#moves the soldier right in the matrix
def move_soldier_right():
    for row in range(len(game_field.final_board()))[::-1]:
        for col in range(len(game_field.final_board()[row])):
            if game_field.final_board()[row][col] == SOLIDER_FEET_BOX:
                game_field.final_board()[row][col] = EMPTY_BOX
                game_field.final_board()[row][col+1] = SOLIDER_FEET_BOX

    for row in range(len(game_field.final_board()))[::-1]:
        for col in range(len(game_field.final_board()[row])):
            if game_field.final_board()[row][col] == SOLIDER_BODY_BOX:
                game_field.final_board()[row][col] = EMPTY_BOX
                game_field.final_board()[row][col - 1] = SOLIDER_BODY_BOX


#moves the soldier up in the matrix
def move_soldier_up():
    for row in range(len(game_field.final_board())):
        for col in range(len(game_field.final_board()[row])):
            if game_field.final_board()[row][col] == SOLIDER_BODY_BOX:
                game_field.final_board()[row][col] = EMPTY_BOX
                game_field.final_board()[row - 1][col] = SOLIDER_BODY_BOX

    for row in range(len(game_field.final_board())):
        for col in range(len(game_field.final_board()[row])):
            if game_field.final_board()[row][col] == SOLIDER_FEET_BOX:
                game_field.final_board()[row][col] = EMPTY_BOX
                game_field.final_board()[row - 1][col] = SOLIDER_FEET_BOX


#moves the soldier down in the matrix
def move_soldier_down(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == SOLIDER_FEET_BOX:
                board[row][col] = EMPTY_BOX
                if row + 1 < len(board):
                    board[row + 1][col] = SOLIDER_FEET_BOX

    for row in range(len(board))[::-1]:
        for col in range(len(board[row])):
            if board[row][col] == SOLIDER_BODY_BOX:
                board[row][col] = EMPTY_BOX
                if row + 1 < len(board):
                    board[row + 1][col] = SOLIDER_BODY_BOX
    return board

