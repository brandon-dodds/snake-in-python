import pygame as pg
import Colours
from Direction import Direction
from Grid import Grid
from Snake import Snake
from RandomObject import RandomObject


def main():
    grid = Grid()
    snake = Snake(15, 15)
    random_object = RandomObject()

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
                    update_grid_to_snake_movement(grid, snake, Direction.LEFT)
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    update_grid_to_snake_movement(grid, snake, Direction.UP)
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    update_grid_to_snake_movement(grid, snake, Direction.DOWN)
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    update_grid_to_snake_movement(grid, snake, Direction.RIGHT)

        screen.fill(Colours.BLACK)

        for row in range(grid.AMOUNT_PER_LINE):
            for column in range(grid.AMOUNT_PER_LINE):
                color = grid.grid[row][column]

                pg.draw.rect(screen,
                             color,
                             [(grid.MARGIN + grid.WIDTH) * column + grid.MARGIN,
                              (grid.MARGIN + grid.HEIGHT) * row + grid.MARGIN,
                              grid.WIDTH,
                              grid.HEIGHT])

        for snake_chunk in snake.snake_body:
            grid.make_colour(snake_chunk[0], snake_chunk[1], Colours.GREEN)

        grid.make_colour(random_object.x_coordinate, random_object.y_coordinate, Colours.RED)
        clock.tick(60)
        pg.display.flip()

    pg.quit()


def update_grid_to_snake_movement(grid, snake, direction):
    for snake_chunk in snake.snake_body:
        grid.make_colour(snake_chunk[0], snake_chunk[1], Colours.WHITE)
    snake.snake_movement(direction)


main()
