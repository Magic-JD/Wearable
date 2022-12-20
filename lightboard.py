import random
from time import sleep

# from unicorn_hat_sim import unicornhat
import unicornhat as uh


class LightBoard:
    pixels = None

    def __init__(self):
        uh.set_layout(uh.AUTO)

    def light_snake(self, snake):
        temp = snake
        while temp is not None:
            uh.set_pixel(temp.x, temp.y, 255, 0, 0)
            temp = temp.tail
        uh.show()

    def light_food(self, food):
        uh.set_pixel(food.x, food.y, 0, 255, 0)
        uh.show()

    def turn_off_snake(self, snake):
        temp = snake
        while temp is not None:
            uh.set_pixel(temp.x, temp.y, 0, 0, 0)
            temp = temp.tail
        uh.show()

    def turn_off_food(self, food):
        uh.set_pixel(food.x, food.y, 0, 0, 0)
        uh.show()

    def flash(self, head):
        for i in range(10):
            self.light_snake(head)
            sleep(0.1)
            self.turn_off_snake(head)
            sleep(0.1)

    def light_all(self):
        for i in range(8):
            for j in range(8):
                uh.set_pixel(i, j, 115, 115, 115)
        uh.show()

    def random_shimmer(self):
        if self.pixels is None:
            self.pixels = []
            for i in range(8):
                for j in range(8):
                    self.pixels.append(uh.get_pixel(i, j))
        self.random_shimmer_post_setup()

    def random_shimmer_post_setup(self):
        j = 0
        for i in range(8):
            #for j in range(8):
                rgb = self.pixels[(i * 8) + j]
                updated = (self.modolate_rgb(rgb[0] + (i + j) + 3), self.modolate_rgb(rgb[1] - (i - j) - 5),
                           self.modolate_rgb(rgb[2] - (i + j) + 8))
                self.pixels[(i * 1) + j] = updated
                r = abs(updated[0])
                g = abs(updated[1])
                b = abs(updated[2])
                print(r)
                print(g)
                print(b)
                uh.set_pixel(i, j, r, g, b)
        uh.show()
        sleep(10)

    def modolate_rgb(self, value):
        if value > 255:
            value = -255 + (value % 255)
        if value < -255:
            value = 255 - (abs(value) % 255)
        return value

    def clear(self):
        for i in range(8):
            for j in range(8):
                uh.set_pixel(i, j, 0, 0, 0)
                uh.show()
