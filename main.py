import threading
from bluedot import BlueDot
from snake_game import Game
from lightboard import LightBoard
from time import sleep

lightboard = LightBoard()
bd = BlueDot()
light_show = True
client_connected = False


def show_lightshow():
    while client_connected and light_show:
        lightboard.random_shimmer()
    lightboard.clear()


light_show_thread = threading.Thread(target=show_lightshow)


def run_connected():
    global light_show
    global light_show_thread
    while client_connected:
        while light_show_thread.is_alive():
            sleep(0.1)
        bd.resize(2, 1)
        button_right = bd[0, 0]
        button_left = bd[1, 0]
        sg = Game()
        button_left.when_pressed = sg.snake.turn_left
        button_right.when_pressed = sg.snake.turn_right
        sg.start_game()
        button_left.when_pressed = None
        button_right.when_pressed = None
        bd.resize(1, 0)
        light_show = True
        light_show_thread.start()


def connect():
    global client_connected
    client_connected = True
    light_show_thread.start()


def disconnect():
    global client_connected
    client_connected = False


def start_game():
    global light_show
    light_show = False
    run_connected()


bd.when_client_connects = connect
bd.when_client_disconnects = disconnect
bd.when_pressed = start_game

while True:
    sleep(3)
