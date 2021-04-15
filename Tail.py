class Tail(object):

    def __init__(self, pos, is_head, color):

        self.pos = pos
        self.is_head = is_head
        self.size = 1

        self.son = None
        self.previous_pos = None

        self.color = color

    def move_up(self):
        self.follow((self.pos[0], self.pos[1] - 1))

    def move_right(self):
        self.follow((self.pos[0] + 1, self.pos[1]))

    def move_down(self):
        self.follow((self.pos[0], self.pos[1] + 1))

    def move_left(self):
        self.follow((self.pos[0] - 1, self.pos[1]))

    # return True if tail is eaten
    def follow(self, new_pos):

        self.previous_pos = self.pos
        self.pos = new_pos

        if self.son is not None:
            self.son.follow(self.previous_pos)

        self.eat_tail()  #  eats the tail if colliding

    def grow(self):
        self.size += 1
        if self.son is None:
            self.son = Tail(self.previous_pos, False, self.color)
        else:
            self.son.grow()

    # return the Father that has eaten the tail
    def check_collision(self):

        actual_father = self
        actual_son = self.son
        while actual_son is not None:
            if self.pos == actual_son.pos:
                self.color = (0, 0, 255)
                return actual_father
            actual_father = actual_son
            actual_son = actual_son.son

        self.color = (0, 255, 0)
        return False

    # If collision happens, eats the tail.
    def eat_tail(self):
        father = self.check_collision()
        if father:
            father.son = None
