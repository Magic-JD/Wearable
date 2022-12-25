import random

from direction import Direction
from food import Food
from snake import SnakeSegment
from lightboard import LightBoard


class Game:
    running = True

    def __init__(self):
        self.snake = SnakeSegment(8, 4, Direction.NORTH)
        self.lightboard = LightBoard()
        self.food = self.generate_food(self.snake.get_positions())

    def generate_food(self, list_pos):
        list_areas = []
        for i in range(8):
            for j in range(8):
                list_areas.append((i, j))
        filtered = [x for x in list_areas if x not in list_pos]
        loc = random.choice(filtered)
        return Food(loc[0], loc[1])

    def run_game_loop(self):
        self.lightboard.turn_off_snake(self.snake)
        self.snake.move()
        if self.snake.x is self.food.x and self.snake.y is self.food.y:
            self.snake.grow()
            self.food = self.generate_food(self.snake.get_positions())
            self.lightboard.light_food(self.food)
        if self.snake.is_overlapping():
            self.running = False
        self.lightboard.light_snake(self.snake)

    def start_game(self):
        self.lightboard.light_snake(self.snake)
        self.lightboard.light_food(self.food)

    def end_game(self):
        self.lightboard.flash(self.snake)
        self.lightboard.turn_off_snake(self.snake)
        self.lightboard.turn_off_food(self.food)
