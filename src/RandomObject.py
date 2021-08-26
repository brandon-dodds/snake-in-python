import random


class RandomObject:
    x_coordinate = 0
    y_coordinate = 0

    def __init__(self, snake_body):
        random_x = random.randint(1, 15)
        random_y = random.randint(1, 15)
        while [random_x, random_y] in snake_body:
            random_x = random.randint(1, 15)
            random_y = random.randint(1, 15)
        self.x_coordinate = random_x
        self.y_coordinate = random_y
