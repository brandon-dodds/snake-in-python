import pygame as pg

import Colours
from Direction import Direction
from GridLogic import GridLogic
from Snake import Snake


def main():
    grid_controller = GridLogic()
    snake = Snake(10, 10)

    pg.init()

    window_size = [308, 308]

    screen = pg.display.set_mode(window_size)

    pg.display.set_caption("Snake Game")

    done = False
    clock = pg.time.Clock()

    while not done:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    grid_white_to_snake(grid_controller, snake)
                    snake.snake_movement(Direction.LEFT)
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    grid_white_to_snake(grid_controller, snake)
                    snake.snake_movement(Direction.UP)
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    grid_white_to_snake(grid_controller, snake)
                    snake.snake_movement(Direction.DOWN)
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    grid_white_to_snake(grid_controller, snake)
                    snake.snake_movement(Direction.RIGHT)

        screen.fill(Colours.BLACK)

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


def grid_white_to_snake(grid, snake):
    for snake_chunk in snake.snake_body:
        grid.make_white(snake_chunk[0], snake_chunk[1])


main()
