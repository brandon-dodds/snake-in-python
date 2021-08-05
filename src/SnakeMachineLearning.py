import pygame as pg

import Colours
from Direction import Direction
from GridLogic import GridLogic
from Snake import Snake


def main():
    grid_controller = GridLogic()
    snake = Snake(10, 10)

    pg.init()

    # The size of the window that will be a constant. Edit if you want the window size to be bigger.
    window_size = [308, 308]

    screen = pg.display.set_mode(window_size)

    pg.display.set_caption("Snake Game")

    # Important variables and declaration of objects.

    done = False
    clock = pg.time.Clock()

    while not done:

        for event in pg.event.get():
            # QUITTING THE PROGRAM.
            if event.type == pg.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    snake.snake_movement(Direction.LEFT)
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    snake.snake_movement(Direction.UP)
            # USER INPUT

        screen.fill(Colours.BLACK)

        # This populates the grid with the white squares. and when a row and a column is equal to one,
        # it turns the colour green.

        for row in range(grid_controller.AMOUNT_PER_LINE):
            for column in range(grid_controller.AMOUNT_PER_LINE):
                color = grid_controller.grid[row][column]

                pg.draw.rect(screen,
                             color,
                             [(grid_controller.MARGIN + grid_controller.WIDTH) * column + grid_controller.MARGIN,
                              (grid_controller.MARGIN + grid_controller.HEIGHT) * row + grid_controller.MARGIN,
                              grid_controller.WIDTH,
                              grid_controller.HEIGHT])

        for snake_chunk in snake.snake_body:
            grid_controller.make_green(snake_chunk[0], snake_chunk[1])

        clock.tick(60)

        pg.display.flip()

    pg.quit()


main()
