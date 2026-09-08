BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

#This page consts
BACKGROUND_COLOR = (138, 201, 38)

import pygame
pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Adi and Roni")
window.fill(BACKGROUND_COLOR)
run = True
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()