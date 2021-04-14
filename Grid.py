import random
from Fruit import Fruit


class Grid:
    def __init__(self, grid_width, grid_height, head):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.head = head
        self.fruit = None
        self.snake_orientation = None

    def move_head_up(self):
        if self.head.pos[1] > 0:
            self.head.move_up()
        else:
            self.head.follow((self.head.pos[0], self.grid_height - 1))

    def move_head_right(self):
        if self.head.pos[0] < self.grid_width - 1:
            self.head.move_right()
        else:
            self.head.follow((0, self.head.pos[1]))

    def move_head_down(self):
        if self.head.pos[1] < self.grid_height - 1:
            self.head.move_down()
        else:
            self.head.follow((self.head.pos[0], 0))

    def move_head_left(self):
        if self.head.pos[0] > 0:
            self.head.move_left()
        else:
            self.head.follow((self.grid_width - 1, self.head.pos[1]))

    def set_orientation(self, new_orientation):
        if self.snake_orientation is None:
            self.snake_orientation = new_orientation

        elif new_orientation == 0:
            if self.snake_orientation != 2:
                self.snake_orientation = 0

        elif new_orientation == 1:
            if self.snake_orientation != 3:
                self.snake_orientation = 1

        elif new_orientation == 2:
            if self.snake_orientation != 0:
                self.snake_orientation = 2

        elif new_orientation == 3:
            if self.snake_orientation != 1:
                self.snake_orientation = 3

    def move_head(self):
        if self.snake_orientation == 0:
            self.move_head_up()
        elif self.snake_orientation == 1:
            self.move_head_right()
        elif self.snake_orientation == 2:
            self.move_head_down()
        elif self.snake_orientation == 3:
            self.move_head_left()

    def generate_fruit(self):
        x = random.randrange(self.grid_width)
        y = random.randrange(self.grid_height)

        self.fruit = Fruit((x, y))

    def check_fruit(self):
        if self.head.pos == self.fruit.pos:
            self.head.grow()
            self.generate_fruit()
