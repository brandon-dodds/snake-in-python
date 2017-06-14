# This project was created by subpanda101 on June the 10th, 2017. May the snake begin!

import pygame as pg

# Define constants for each individual colour.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (42, 201, 42)
HEIGHT = 16
WIDTH = 16
MARGIN = 3
AMOUNT_PER_LINE = 16

# Create the grid.

grid = []
for row in range(AMOUNT_PER_LINE):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(AMOUNT_PER_LINE):
        grid[row].append(0)  # Append a cell

newX = 0
newY = 0


def snake(x, y):
    grid[x][y] = 1
    global newX
    newX = x
    global newY
    newY = y


pg.init()

WINDOW_SIZE = [308, 308]

screen = pg.display.set_mode(WINDOW_SIZE)

pg.display.set_caption("Snake Game")

done = False

clock = pg.time.Clock()

snake(8, 8)

while not done:

    for event in pg.event.get():
        if event.type == pg.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif pg.key.get_pressed()[pg.K_w] != 0:
            print("UP")
            grid[newX][newY] = 0
            snake(newX - 1, newY)
        elif pg.key.get_pressed()[pg.K_a] != 0:
            print("LEFT")
            grid[newX][newY] = 0
            snake(newX, newY - 1)
        elif pg.key.get_pressed()[pg.K_s] != 0:
            print("DOWN")
            grid[newX][newY] = 0
            snake(newX + 1, newY)
        elif pg.key.get_pressed()[pg.K_d] != 0:
            print("RIGHT")
            grid[newX][newY] = 0
            snake(newX, newY + 1)

    screen.fill(BLACK)

    # Define the amount of white squares per line.
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
