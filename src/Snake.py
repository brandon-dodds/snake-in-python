from collections import deque
from Direction import Direction


class Snake:
    snake_body = []
    movementList = deque([])
    direction = Direction.UP

    def __init__(self, x_coordinate, y_coordinate):  # This is executed when a snake is created.
        self.snake_body.append([x_coordinate, y_coordinate])

    def snake_movement(self, direction):
        self.movementList.append(direction)

        for chunk in self.snake_body:
            for movement in self.movementList:

                if movement == Direction.UP:
                    chunk[0] = chunk[0] - 1
                    self.direction = Direction.UP

                elif movement == Direction.DOWN:
                    chunk[0] = chunk[0] + 1
                    self.direction = Direction.DOWN

                elif movement == Direction.LEFT:
                    chunk[1] = chunk[1] - 1
                    self.direction = Direction.LEFT

                elif movement == Direction.RIGHT:
                    chunk[1] = chunk[1] + 1
                    self.direction = Direction.RIGHT
