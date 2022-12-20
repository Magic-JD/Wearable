import random
import threading
from time import sleep

import bluedot as bd
from direction import Direction
from food import Food
from snake import SnakeSegment
from lightboard import LightBoard


class Game:
    running = True

    def __init__(self):
        self.snake = SnakeSegment(0, 4, Direction.EAST)
    #  self.bd = bd
      #  self.button_left = bd[0, 0]
      #  self.button_right = bd[1, 0]
      #  self.button_left.when_pressed = self.snake.turn_left()
      #  self.button_right.when_pressed = self.snake.turn_right()

    def generate_food(self, list_pos):
        list_areas = []
        for i in range(8):
            for j in range(8):
                list_areas.append((i, j))
        filtered = [x for x in list_areas if x not in list_pos]
        loc = random.choice(filtered)
        return Food(loc[0], loc[1])

    def run_game_loop(self):
        lightboard = LightBoard()
        food = self.generate_food(self.snake.get_positions())
        lightboard.light_snake(self.snake)
        lightboard.light_food(food)
        while self.running:
            lightboard.turn_off_snake(self.snake)
            self.snake.move()
            if self.snake.x is food.x and self.snake.y is food.y:
                self.snake.grow()
                food = self.generate_food(self.snake.get_positions())
                lightboard.light_food(food)
            if self.snake.is_overlapping():
                running = False
            lightboard.light_snake(self.snake)
            sleep(0.3)
        lightboard.flash(self.snake)
        lightboard.turn_off_snake(self.snake)
        lightboard.turn_off_food(food)

    def start_game(self):
        self.run_game_loop()
