import threading

import keyboard

from snake_game import start_game
from lightboard import LightBoard

lightboard = LightBoard()
lightboard.light_all()

waiting_for_input = True


def get_user_input():
    global waiting_for_input
    while waiting_for_input:
        if keyboard.is_pressed("a"):
            print("awaited_input")
            waiting_for_input = False


waiting_input_thread = threading.Thread(target=get_user_input).start()
while True:
    while waiting_for_input:
        lightboard.random_shimmer()
    lightboard.clear()
    start_game()
    waiting_for_input = True
    waiting_input_thread = threading.Thread(target=get_user_input).start()


