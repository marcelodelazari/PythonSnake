import pygame

from Drawer import Drawer
from Grid import Grid
from Tail import Tail

pygame.init()


# TODO: Pontuaçao atual e pontuaçao maxima

def set_player_orientation(new_orientation):
    grid.set_orientation(new_orientation)


def move_player():
    grid.move_head()


def check_fruit():
    grid.check_fruit()


def next_frame():
    global moved_in_this_frame

    move_player()
    moved_in_this_frame = False
    check_fruit()


#  Sreen Setup
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Snake")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game variables
game_size = 5  # set WIDTH and HEIGHT divisor for proper screen
grid_width = 4 * game_size
grid_height = 3 * game_size
head_width = WIDTH // grid_width
head_height = HEIGHT // grid_height
head_pos = (grid_width // 2, grid_height // 2)
orientation = None
grid_on = False

# Instanciate classes
head = Tail(head_pos, True, GREEN)
grid = Grid(grid_width, grid_height, head)
drawer = Drawer(screen, WIDTH, HEIGHT, grid, head)
grid.generate_fruit()

# Game loop
running = True
clock = pygame.time.Clock()
moved_in_this_frame = False
paused = False
framerate = 15

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not moved_in_this_frame and not paused:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    set_player_orientation(0)
                    moved_in_this_frame = True
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    set_player_orientation(1)
                    moved_in_this_frame = True
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    set_player_orientation(2)
                    moved_in_this_frame = True
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    set_player_orientation(3)
                    moved_in_this_frame = True

            if event.key == pygame.K_p:
                paused = not paused

            elif event.key == pygame.K_g:
                grid_on = not grid_on

            elif not paused and event.key == pygame.K_h:
                head.grow()

    if not paused:
        next_frame()

    drawer.draw(grid_on, paused)
    clock.tick(framerate)
