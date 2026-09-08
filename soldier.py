import consts
import game_field

from consts import *

def move_soldier_left():
    for row in range(len(game_field.final_board())):
        for col in range(len(game_field.final_board()[row])):
            if game_field.final_board()[row][col] == SOLIDER_BOX:
                game_field.final_board()[row][col] = EMPTY_BOX
                game_field.final_board()[row][col+1] = SOLIDER_BOX




def move_soldier_right():
    for row in range(len(game_field.final_board()),0):
        for col in range(len(game_field.final_board()[row]),0):
            if game_field.final_board()[row][col] == SOLIDER_BOX:
                game_field.final_board()[row][col] = EMPTY_BOX
                game_field.final_board()[row][col - 1] = SOLIDER_BOX

def move_soldier_up():
    pass

def move_soldier_down():
    pass


