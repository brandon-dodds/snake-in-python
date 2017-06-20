# This project was created by subpanda101 on June the 10th, 2017. May the snake begin!

import pygame as pg

# Defining colour constants.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (42, 201, 42)
HEIGHT = 16
WIDTH = 16
MARGIN = 3
AMOUNT_PER_LINE = 16

# Creating the grid that will be populated.

grid = []
for row in range(AMOUNT_PER_LINE):
    grid.append([])
    for column in range(AMOUNT_PER_LINE):
        grid[row].append(0)  # Creates a 2d array which my grid will be based.

# Some global variables.

pg.init()

# The size of the window that will be a constant. Edit if you want the window size to be bigger.

WINDOW_SIZE = [308, 308]

screen = pg.display.set_mode(WINDOW_SIZE)

pg.display.set_caption("Snake Game")

done = False

clock = pg.time.Clock()

# Creates a snake at the coordinates [8,8].


while not done:

    for event in pg.event.get():
        # QUITTING THE PROGRAM.
        if event.type == pg.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        # USER INPUT.
        elif pg.key.get_pressed()[pg.K_q] != 0:
            done = True

    screen.fill(BLACK)

    # This populates the grid with the white squares. and when a row and a column is equal to one,
    # it turns the colour green.

    for row in range(AMOUNT_PER_LINE):
        for column in range(AMOUNT_PER_LINE):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pg.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    clock.tick(60)

    pg.display.flip()

pg.quit()
