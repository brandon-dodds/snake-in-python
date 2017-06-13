# This project was created by subpanda101 on June the 10th, 2017. May the snake begin!

import pygame as pg

# Define constants for each individual colour.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HEIGHT = 16
WIDTH = 16
MARGIN = 1
AMOUNT_PER_LINE = 16

# Create the grid.

grid = []
for row in range(AMOUNT_PER_LINE):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(AMOUNT_PER_LINE):
        grid[row].append(0)  # Append a cell

pg.init()

WINDOW_SIZE = [272, 272]

screen = pg.display.set_mode(WINDOW_SIZE)

pg.display.set_caption("Snake Game")

done = False

clock = pg.time.Clock()

while not done:

    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            print("Exiting...")
            done = True

    screen.fill(BLACK)

    # Define the amount of white squares per line.
    for row in range(AMOUNT_PER_LINE):
        for column in range(AMOUNT_PER_LINE):
            color = WHITE
            pg.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    clock.tick(60)

    pg.display.flip()

pg.quit()
