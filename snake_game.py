import random
import threading
from time import sleep
import keyboard

from direction import Direction
from food import Food
from snake import SnakeSegment
from lightboard import LightBoard

running = True
snake = SnakeSegment(0, 4, Direction.EAST)

def get_user_input():
    global running
    while running:
        if keyboard.is_pressed("a"):
            snake.turn_left()
        if keyboard.is_pressed("d"):
            snake.turn_right()
        sleep(0.1)


def generate_food(list_pos):
    list_areas = []
    for i in range(7):
        for j in range(7):
            list_areas.append((i, j))
    filtered = [x for x in list_areas if x not in list_pos]
    loc = random.choice(filtered)
    return Food(loc[0], loc[1])


def run_game_loop():
    global running
    lightboard = LightBoard()
    food = generate_food(snake.get_positions())
    lightboard.light_snake(snake)
    lightboard.light_food(food)
    while running:
        lightboard.turn_off_snake(snake)
        snake.move()
        if snake.x is food.x and snake.y is food.y:
            snake.grow()
            food = generate_food(snake.get_positions())
            lightboard.light_food(food)
        if snake.is_overlapping():
            running = False
        lightboard.light_snake(snake)
        sleep(0.3)
    lightboard.flash(snake)
    lightboard.turn_off_snake(snake)
    lightboard.turn_off_food(food)

def start_game():
    threading.Thread(target=get_user_input).start()
    game_thread = threading.Thread(target=run_game_loop)
    game_thread.start()
    game_thread.join()
