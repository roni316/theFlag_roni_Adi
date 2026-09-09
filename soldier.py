import game_field
import screen
from consts import *

def find_feet():
    feet_location = []
    location = ()
    for row in range(len(game_field.final_board())):
        for col in range(len(game_field.final_board()[row])):
            if game_field[row][col] == SOLIDER_FEET_BOX:
                location = (row,col)
            feet_location.append(location)
    return feet_location


def find_body():
    body_location = []
    location = ()
    for row in range(len(game_field.final_board())):
        for col in range(len(game_field.final_board()[row])):
            if game_field[row][col] == SOLIDER_BODY_BOX:
                location = (row,col)
            body_location.append(location)
    return body_location



#moves the soldier left in the matrix
def move_soldier_left(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == SOLIDER_BODY_BOX:
                if board[row][col - 1] == EMPTY_BOX:
                    board[row][col] = EMPTY_BOX
                    board[row][col - 1] = SOLIDER_BODY_BOX
                if board[row][col -1] == FLAG_BOX:
                    screen.win()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == SOLIDER_FEET_BOX:
                if board[row][col - 1] == EMPTY_BOX:
                    board[row][col] = EMPTY_BOX
                    board[row][col - 1] = SOLIDER_FEET_BOX
                if board[row][col - 1] == MINE_BOX:
                    screen.lose()

    for i in board:
        print(i)
    return board


#moves the soldier right in the matrix
def move_soldier_right(board):
    for row in range(len(board))[::-1]:
        for col in range(len(board[row])):
            if board[row][col] == SOLIDER_FEET_BOX:
                if board[row][col + 1] == EMPTY_BOX:
                    board[row][col] = EMPTY_BOX
                    board[row][col + 1] = SOLIDER_FEET_BOX
                if board[row][col + 1] == MINE_BOX:
                    screen.lose()

    for row in range(len(board))[::-1]:
        for col in range(len(board[row])):
            if board[row][col] == SOLIDER_BODY_BOX:
                if board[row][col + 1] == EMPTY_BOX:
                    board[row][col] = EMPTY_BOX
                    board[row][col + 1] = SOLIDER_FEET_BOX
                if board[row][col + 1] == MINE_BOX:
                    screen.lose()
    for i in board:
        print(i)
    return board

#moves the soldier up in the matrix
def move_soldier_up(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == SOLIDER_BODY_BOX:
                if board[row - 1][col] == EMPTY_BOX:
                    board[row][col] = EMPTY_BOX
                    board[row - 1][col] = SOLIDER_BODY_BOX
                if board[row - 1][col] == FLAG_BOX:
                    screen.win()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == SOLIDER_FEET_BOX:
                if board[row - 1][col] == EMPTY_BOX:
                    board[row][col] = EMPTY_BOX
                    board[row - 1][col] = SOLIDER_FEET_BOX
                if board[row - 1][col] == MINE_BOX:
                    screen.lose()
    for i in board:
        print(i)
    return board


#moves the soldier down in the matrix
def move_soldier_down(board):
    count = 0
    for row in range(len(board))[::-1]:
        for col in range(len(board[row])):
                if board[row][col] == SOLIDER_FEET_BOX:
                    if board[row + 1][col] == EMPTY_BOX :
                        board[row][col] = EMPTY_BOX
                        board[row + 1][col] = SOLIDER_FEET_BOX
                    if board[row + 1][col] == MINE_BOX:
                        screen.lose()

    for row in range(len(board))[::-1]:
        for col in range(len(board[row])):
            if board[row][col] == SOLIDER_BODY_BOX :
                if board[row + 1][col] == EMPTY_BOX:
                    board[row][col] = EMPTY_BOX
                    board[row + 1][col] = SOLIDER_BODY_BOX
                if board[row + 1][col] == FLAG_BOX:
                    screen.win()

    for i in board:
        print(i)
    return board


