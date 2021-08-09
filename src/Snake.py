from collections import deque
from Direction import Direction


class Snake:
    snake_body = []
    movementList = deque([])

    def __init__(self, x_coordinate, y_coordinate):
        self.snake_body.append([x_coordinate, y_coordinate])

    def snake_movement(self, direction):
        self.movementList.appendleft(direction)

        for chunk in self.snake_body:

            if self.movementList[self.snake_body.index(chunk)] == Direction.UP:
                chunk[0] = chunk[0] - 1

            elif self.movementList[self.snake_body.index(chunk)] == Direction.DOWN:
                chunk[0] = chunk[0] + 1

            elif self.movementList[self.snake_body.index(chunk)] == Direction.LEFT:
                chunk[1] = chunk[1] - 1

            elif self.movementList[self.snake_body.index(chunk)] == Direction.RIGHT:
                chunk[1] = chunk[1] + 1

    def snake_check_self_collision(self):
        for chunk in self.snake_body[1:]:
            return chunk == self.snake_body[0]

    def snake_add_body(self):
        self.snake_body.append([self.snake_body[0][0], self.snake_body[0][1]])
