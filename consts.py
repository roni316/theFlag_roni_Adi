import pygame.image

BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20

WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3
SOLDIER_FEET_ROWS = 1

FLAG_ROWS = 3
FLAG_COLS = 4

MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3

RUNNING_STATE = 1
LOSE_STATE = 2
WIN_STATE = 3

BACKGROUND_COLOR = (0, 100, 0)
EXPLOSION = pygame.image.load('explotion.png')
FLAG = pygame.image.load('flag.png')
GRASS = pygame.image.load('grass.png')
GUARD = pygame.image.load('guard.png')
INJURY = pygame.image.load('injury.png')
MINE = pygame.image.load('mine.png')
SNAKE = pygame.image.load('snake.png')
SOLIDER = pygame.image.load('soldier.png')
SOLIDER_NIGHT = pygame.image.load('soldier_night.png')
TELEPORT = pygame.image.load('teleport.png')

SOLIDER_WIDTH = SOLDIER_COLS * CELL_SIZE
SOLIDER_HEIGHT = SOLDIER_ROWS * CELL_SIZE

FLAG_WIDTH = FLAG_COLS * CELL_SIZE
FLAG_HEIGHT = FLAG_ROWS * CELL_SIZE
FLAG_ROW_DES = BOARD_ROWS - FLAG_ROWS
FLAG_COL_DES = BOARD_COLS - FLAG_COLS

GRASS_WIDTH = MINE_COLS * CELL_SIZE
GRASS_HEIGHT = MINE_ROWS * CELL_SIZE


EMPTY_BOX = "EMPTY"
MINE_BOX = "MINE"
SOLIDER_BODY_BOX = "SOLDIER_BODY"
SOLIDER_FEET_BOX = "SOLDIER_FEET"
FLAG_BOX = "FLAG"