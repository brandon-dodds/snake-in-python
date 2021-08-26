from collections import deque
from Direction import Direction


class Snake:
    snake_body = []
    movement_list = deque([])
    last_chunk_previous_movement = []

    def __init__(self, x_coordinate, y_coordinate):
        self.snake_body.append([x_coordinate, y_coordinate])
        self.last_chunk_previous_movement = self.snake_body[-1].copy()

    def snake_movement(self, direction):
        self.movement_list.appendleft(direction)
        self.last_chunk_previous_movement = self.snake_body[-1].copy()
        for chunk in self.snake_body:

            if self.movement_list[self.snake_body.index(chunk)] == Direction.UP and chunk[0] - 1 >= 0:
                chunk[0] = chunk[0] - 1

            elif self.movement_list[self.snake_body.index(chunk)] == Direction.DOWN and chunk[0] + 1 <= 15:
                chunk[0] = chunk[0] + 1

            elif self.movement_list[self.snake_body.index(chunk)] == Direction.LEFT and chunk[1] - 1 >= 0:
                chunk[1] = chunk[1] - 1

            elif self.movement_list[self.snake_body.index(chunk)] == Direction.RIGHT and chunk[1] + 1 <= 15:
                chunk[1] = chunk[1] + 1
