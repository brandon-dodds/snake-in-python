from collections import deque
from Direction import Direction


class Snake:
    snake_body = []
    movementList = deque([])

    def __init__(self, x_coordinate, y_coordinate):  # This is executed when a snake is created.
        self.snake_body.append([x_coordinate, y_coordinate])

    def snake_movement(self, direction):
        self.movementList.appendleft(direction)

        for chunk in self.snake_body:
            for movement in range(len(self.snake_body)):

                if self.movementList[movement] == Direction.UP:
                    chunk[0] = chunk[0] - 1

                elif self.movementList[movement] == Direction.DOWN:
                    chunk[0] = chunk[0] + 1

                elif self.movementList[movement] == Direction.LEFT:
                    chunk[1] = chunk[1] - 1

                elif self.movementList[movement] == Direction.RIGHT:
                    chunk[1] = chunk[1] + 1
