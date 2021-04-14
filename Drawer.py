import pygame


class Drawer(object):

    WHITE = (255, 255, 255)
    GREY = (200, 200, 200)
    BLACK = (0, 0, 0)
    GREEN = (20, 200, 20)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (150, 150, 0)

    def __init__(self, screen, width, height, grid, head):
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height

        self.grid = grid
        self.grid_width_div_size = self.WIDTH // self.grid.grid_width
        self.grid_height_div_size = self.HEIGHT // self.grid.grid_height

        self.head = head

        self.pause_font = pygame.font.SysFont("Comic Sans MS", 100)
        self.pause_label = self.pause_font.render("Paused", True, self.YELLOW)
        self.pause_rect = self.pause_label.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))

    def draw(self, grid_on, paused):
        self.screen.fill(self.BLACK)

        self.draw_snake()
        self.draw_fruit()

        if grid_on:
            self.draw_grid()

        if paused:
            self.screen.blit(self.pause_label, self.pause_rect)

        pygame.display.update()

    def draw_grid(self):
        for x in range(0, self.WIDTH, self.grid_width_div_size):
            pygame.draw.line(self.screen, self.GREY, (x, 0), (x, self.HEIGHT))
        for y in range(0, self.HEIGHT, self.grid_height_div_size):
            pygame.draw.line(self.screen, self.GREY, (0, y), (self.WIDTH, y))

    def draw_snake(self):

        actual_tail = self.head
        while actual_tail is not None:
            self.draw_block(actual_tail, self.head.color)
            actual_tail = actual_tail.son

    def draw_fruit(self):
        self.draw_block(self.grid.fruit, self.RED)

    def draw_block(self, block, color):
        if block is not None:
            block_screen_x = self.grid_width_div_size * block.pos[0]
            block_screen_y = self.grid_height_div_size * block.pos[1]
            pygame.draw.rect(
                self.screen, color, (block_screen_x, block_screen_y, self.grid_width_div_size, self.grid_height_div_size))
