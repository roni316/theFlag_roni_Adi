import consts
import pygame


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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                night_vision()

        if event.key == pygame.K_LEFT:
            move_soldier()

        if event.key == pygame.K_RIGHT:
            move_soldier()

        if event.key == pygame.K_UP:
            move_soldier()

        if event.key == pygame.K_DOWN:
            move_soldier()


def move_soldier():
    pass

def night_vision():
    pass