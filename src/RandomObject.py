import random


class RandomObject:
    x_coordinate = 0
    y_coordinate = 0

    def __init__(self):
        self.x_coordinate = random.randint(1, 15)
        self.y_coordinate = random.randint(1, 15)
        if snakeList[0].x_coordinate == self.x_coordinate and snakeList[0].y_coordinate == self.y_coordinate:
            self.__init__()

        grid[self.x_coordinate][self.y_coordinate] = 2

    def new_item(self):
        self.x_coordinate = random.randint(1, 15)
        self.y_coordinate = random.randint(1, 15)
        for x in range(len(snakeList)):
            if self.x_coordinate == snakeList[x].x_coordinate and self.y_coordinate == snakeList[x].y_coordinate:
                self.new_item()

        grid[self.x_coordinate][self.y_coordinate] = 2
