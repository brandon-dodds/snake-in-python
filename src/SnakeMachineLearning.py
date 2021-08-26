import sys

import pygame as pg
import Colours
from Direction import Direction
from Grid import Grid
from Snake import Snake
from RandomObject import RandomObject


def game_exit():
    pg.quit()
    sys.exit()


class Game:
    def __init__(self):
        self.grid = Grid()
        self.snake = Snake(15, 15)
        self.random_object = RandomObject(self.snake.snake_body)

        pg.init()
        window_size = [308, 308]
        self.screen = pg.display.set_mode(window_size)
        pg.display.set_caption("Snake Game")
        self.done = False
        self.clock = pg.time.Clock()

    def render(self):
        self.screen.fill(Colours.BLACK)

        for row in range(self.grid.AMOUNT_PER_LINE):
            for column in range(self.grid.AMOUNT_PER_LINE):
                color = self.grid.grid[row][column]

                pg.draw.rect(self.screen,
                             color,
                             [(self.grid.MARGIN + self.grid.WIDTH) * column + self.grid.MARGIN,
                              (self.grid.MARGIN + self.grid.HEIGHT) * row + self.grid.MARGIN,
                              self.grid.WIDTH,
                              self.grid.HEIGHT])

        for snake_chunk in self.snake.snake_body:
            self.grid.make_colour(snake_chunk[0], snake_chunk[1], Colours.GREEN)

        if self.random_object is not None:
            self.grid.make_colour(self.random_object.x_coordinate, self.random_object.y_coordinate, Colours.RED)

        self.clock.tick(60)
        pg.display.flip()

    def update_grid_to_snake_movement(self, direction):
        for snake_chunk in self.snake.snake_body:
            self.grid.make_colour(snake_chunk[0], snake_chunk[1], Colours.WHITE)
        self.snake.snake_movement(direction)

    def snake_object_collision(self):
        if self.random_object is None:
            return False
        return self.snake.snake_body[0] == [self.random_object.x_coordinate, self.random_object.y_coordinate]

    def check_collisions(self):
        if self.snake_object_collision() and len(self.snake.snake_body) < 256:
            self.snake.snake_body.append(
                [self.snake.last_chunk_previous_movement[0], self.snake.last_chunk_previous_movement[1]])
            self.random_object = RandomObject(self.snake.snake_body)
        else:
            game_exit()
        if self.snake.snake_body[0] in self.snake.snake_body[1:]:
            game_exit()

    def main(self):
        while not self.done:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT or event.key == pg.K_a:
                        self.update_grid_to_snake_movement(Direction.LEFT)
                    elif event.key == pg.K_UP or event.key == pg.K_w:
                        self.update_grid_to_snake_movement(Direction.UP)
                    elif event.key == pg.K_DOWN or event.key == pg.K_s:
                        self.update_grid_to_snake_movement(Direction.DOWN)
                    elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                        self.update_grid_to_snake_movement(Direction.RIGHT)
                    self.check_collisions()

            self.render()

        pg.quit()


game = Game()
game.main()
