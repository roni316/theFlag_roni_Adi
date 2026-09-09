import consts
import pygame
import soldier

state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
}



def main():
    while state["is_window_open"]:

        handle_user_events()






def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.key == pygame.K_LEFT:
            soldier.move_soldier_left()

        if event.key == pygame.K_RIGHT:
            soldier.move_soldier_right()

        if event.key == pygame.K_UP:
            soldier.move_soldier_up()

        if event.key == pygame.K_DOWN:
            soldier.move_soldier_down()




pygame.init()
