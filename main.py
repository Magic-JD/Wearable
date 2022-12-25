from bluedot import BlueDot
from snake_game import Game
from lightboard import LightBoard
from time import sleep

lightboard = LightBoard()
bd = BlueDot()
light_show = True
client_connected = False

lightboard.power_up()

def show_lightshow():
    lightboard.random_shimmer_setup()
    while client_connected and light_show:
        lightboard.random_shimmer()
    lightboard.clear()


def connect():
    global client_connected
    client_connected = True


def disconnect():
    global client_connected
    client_connected = False


def start_game():
    global light_show
    light_show = False


bd.when_client_connects = connect
bd.when_client_disconnects = disconnect
bd[0, 0].when_pressed = start_game

while True:
    while not client_connected:
        sleep(1)

    while client_connected:
        show_lightshow()
        if client_connected:
            bd[0, 0].when_pressed = None
            bd.resize(3, 3)
            bd[0, 0].visible = False
            bd[0, 2].visible = False
            bd[2, 2].visible = False
            bd[2, 0].visible = False
            bd[1, 1].visible = False
            button_up = bd[1, 0]
            button_right = bd[2, 1]
            button_left = bd[0, 1]
            button_down = bd[1, 2]
            sg = Game()
            button_up.when_pressed = sg.snake.turn_up
            button_down.when_pressed = sg.snake.turn_down
            button_right.when_pressed = sg.snake.turn_right
            button_left.when_pressed = sg.snake.turn_left
            sg.start_game()
            while sg.running and client_connected:
                sg.run_game_loop()
                sleep(0.3)
            sg.end_game()
            button_up.when_pressed = None
            button_down.when_pressed = None
            button_right.when_pressed = None
            button_left.when_pressed = None
            bd.resize(1, 1)
            bd[0, 0].when_pressed = start_game
            light_show = True
