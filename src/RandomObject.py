import random


class RandomObject:
    x_coordinate = 0
    y_coordinate = 0

    def __init__(self, snake_body, grid_amount):
        random_x = random.randint(0, grid_amount - 1)
        random_y = random.randint(0, grid_amount - 1)
        while [random_x, random_y] in snake_body:
            random_x = random.randint(0, grid_amount - 1)
            random_y = random.randint(0, grid_amount - 1)
        self.x_coordinate = random_x
        self.y_coordinate = random_y
