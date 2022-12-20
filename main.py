import threading

from bluedot import BlueDot
from snake_game import Game
from lightboard import LightBoard

lightboard = LightBoard()
lightboard.light_all()
bd = BlueDot()
waiting_for_input = True

def reset():
    global waiting_for_input
    print("pressed")
    waiting_for_input = False


bd.when_pressed=reset

while True:
    while waiting_for_input:
        lightboard.random_shimmer()
    lightboard.clear()
    bd.resize(2, 1)
    button_right = bd[0, 0]
    button_left = bd[1, 0]
    sg = Game()
    button_left.when_pressed=sg.snake.turn_left
    button_right.when_pressed=sg.snake.turn_right
    sg.start_game()
    bd.when_pressed=reset
    waiting_for_input = True


