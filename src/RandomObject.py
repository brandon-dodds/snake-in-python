import random


class RandomObject:
    x_coordinate = 0
    y_coordinate = 0

    def __init__(self):
        self.x_coordinate = random.randint(0, 15)
        self.y_coordinate = random.randint(0, 15)
