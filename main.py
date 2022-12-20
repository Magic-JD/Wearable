from bluedot import BlueDot
from snake_game import Game
from lightboard import LightBoard
from time import sleep

lightboard = LightBoard()
bd = BlueDot()
waiting_for_input = True
client_connected = False


def run_connected():
    global waiting_for_input
    while client_connected:
        while waiting_for_input:
            lightboard.random_shimmer()
        lightboard.clear()
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
        waiting_for_input = True


def connect():
    global client_connected
    client_connected = True
    run_connected()


def disconnect():
    global client_connected
    client_connected = False


def start_game():
    global waiting_for_input
    waiting_for_input = False


bd.when_client_connects = connect
bd.when_client_disconnects = disconnect
bd.when_pressed = start_game

while True:
    sleep(3)
