import threading

from bluedot import BlueDot
from snake_game import start_game
from lightboard import LightBoard

lightboard = LightBoard()
lightboard.light_all()
bd = BlueDot()

waiting_for_input = True


def get_user_input():
    global waiting_for_input
    bd.wait_for_press()
    waiting_for_input = False


waiting_input_thread = threading.Thread(target=get_user_input).start()
while True:
    while waiting_for_input:
        lightboard.random_shimmer()
    lightboard.clear()
    bd.rows(2)
    start_game(bd)
    waiting_for_input = True
    waiting_input_thread = threading.Thread(target=get_user_input).start()


