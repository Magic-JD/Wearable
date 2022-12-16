from direction import Direction


class SnakeSegment:
    tail = None
    DIMENSION = 8
    has_turned = False

    def __init__(self, x, y, direction=None):
        self.x = x
        self.y = y
        self.old_x = x
        self.old_y = y
        self.direction = direction

    def turn_left(self):
        if not self.has_turned:
            self.direction = Direction(((self.direction.value + 4) - 1) % 4)
        self.has_turned = True

    def turn_right(self):
        if not self.has_turned:
            self.direction = Direction((self.direction.value + 1) % 4)
        self.has_turned = True

    def move(self):
        self.has_turned = False
        if self.direction is Direction.NORTH:
            self.move_north()
        if self.direction is Direction.EAST:
            self.move_east()
        if self.direction is Direction.SOUTH:
            self.move_south()
        if self.direction is Direction.WEST:
            self.move_west()

    def move_north(self):
        self.move_internal(self.x, (self.y + 1) % self.DIMENSION)

    def move_east(self):
        self.move_internal((self.x + 1) % self.DIMENSION, self.y)

    def move_south(self):
        self.move_internal(self.x, (self.y - 1) if self.y > 0 else self.DIMENSION - 1)

    def move_west(self):
        self.move_internal((self.x - 1) if self.x > 0 else self.DIMENSION - 1, self.y)

    def move_internal(self, x, y):
        self.old_x = self.x
        self.old_y = self.y
        self.x = x
        self.y = y
        if self.tail is not None:
            self.tail.move_internal(self.old_x, self.old_y)

    def grow(self):
        if self.tail is None:
            self.tail = SnakeSegment(self.old_x, self.old_y)
        else:
            self.tail.grow()

    def is_overlapping(self):
        list_p = self.get_positions()
        set_p = set(list_p)
        return not len(list_p) is len(set_p)

    def get_positions(self):
        if self.tail is None:
            return [(self.x, self.y)]
        else:
            list_p = self.tail.get_positions()
            list_p.append((self.x, self.y))
            return list_p
