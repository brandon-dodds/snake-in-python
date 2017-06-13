# This project was created by subpanda101 on June the 10th, 2017. May the snake begin!
import torch as tc
import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HEIGHT = 5
WIDTH = 5
MARGIN = 3


grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

grid[1][5] = 1
pg.init()
WINDOW_SIZE = [64,64]
screen = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption("Snake Game")
done=False
clock = pg.time.Clock()
while not done:
    screen.fill(BLACK)

    clock.tick(60)
    pg.display.flip()

pg.quit()
