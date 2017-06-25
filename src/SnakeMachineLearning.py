import random

import pygame as pg

# Defining colour constants.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (42, 201, 42)
RED = (240, 34, 54)
HEIGHT = 16
WIDTH = 16
MARGIN = 3
AMOUNT_PER_LINE = 16

# Creating the grid that will be populated.

grid = []
for row in range(AMOUNT_PER_LINE):
    grid.append([])
    for column in range(AMOUNT_PER_LINE):
        grid[row].append(0)  # Creates a 2d array which my grid will be based.


# Creating the snakeList object.

class Snake:
    x_coordinate = 0
    y_coordinate = 0
    direction = "UP"

    def __init__(self, x_coordinate, y_coordinate):
        grid[x_coordinate][y_coordinate] = 1
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        print(self.x_coordinate)
        print(self.y_coordinate)

    def move_snake(self, direction):
        if direction == "UP":
            old_x = self.x_coordinate
            old_y = self.y_coordinate
            grid[old_x][old_y] = 0
            grid[old_x - 1][old_y] = 1
            self.x_coordinate = old_x - 1
            print("UP")
            self.direction = "UP"
        elif direction == "DOWN":
            old_x = self.x_coordinate
            old_y = self.y_coordinate
            grid[old_x][old_y] = 0
            grid[old_x + 1][old_y] = 1
            self.x_coordinate = old_x + 1
            print("DOWN")
            self.direction = "DOWN"
        elif direction == "LEFT":
            old_x = self.x_coordinate
            old_y = self.y_coordinate
            grid[old_x][old_y] = 0
            grid[old_x][old_y - 1] = 1
            self.y_coordinate = old_y - 1
            print("LEFT")
            self.direction = "LEFT"
        elif direction == "RIGHT":
            old_x = self.x_coordinate
            old_y = self.y_coordinate
            grid[old_x][old_y] = 0
            grid[old_x][old_y + 1] = 1
            self.y_coordinate = old_y + 1
            print("RIGHT")
            self.direction = "RIGHT"


# Creating the random item object.

class RandomObject(object):
    x_coordinate = 0
    y_coordinate = 0

    def __init__(self):
        self.x_coordinate = random.randint(1, 15)
        self.y_coordinate = random.randint(1, 15)
        grid[self.x_coordinate][self.y_coordinate] = 2

    def new_item(self):
        grid[self.x_coordinate][self.y_coordinate] = 1
        self.x_coordinate = random.randint(1, 15)
        self.y_coordinate = random.randint(1, 15)
        grid[self.x_coordinate][self.y_coordinate] = 2


# Beginning pygame.
pg.init()

# The size of the window that will be a constant. Edit if you want the window size to be bigger.

WINDOW_SIZE = [308, 308]

screen = pg.display.set_mode(WINDOW_SIZE)

pg.display.set_caption("snakeList Game")

# Important variables and declaration of objects.
current_snake = 0
score = 0
snakeList = []
for count in range(1):
    x = Snake(8, 8)
    x.attr = count
    snakeList.append(x)

randomItem = RandomObject()
done = False
clock = pg.time.Clock()

while not done:

    for event in pg.event.get():
        # QUITTING THE PROGRAM.
        if event.type == pg.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        # USER INPUT.s
        elif pg.key.get_pressed()[pg.K_q] != 0:
            done = True

        elif pg.key.get_pressed()[pg.K_w] or pg.key.get_pressed()[pg.K_UP]:
            for n in range((len(snakeList))):
                snakeList[n].move_snake("UP")

        elif pg.key.get_pressed()[pg.K_s] or pg.key.get_pressed()[pg.K_DOWN]:
            for n in range((len(snakeList))):
                snakeList[n].move_snake("DOWN")

        elif pg.key.get_pressed()[pg.K_a] or pg.key.get_pressed()[pg.K_LEFT]:
            for n in range((len(snakeList))):
                snakeList[n].move_snake("LEFT")

        elif pg.key.get_pressed()[pg.K_d] or pg.key.get_pressed()[pg.K_RIGHT]:
            for n in range((len(snakeList))):
                snakeList[n].move_snake("RIGHT")

        # CONTROL STATEMENTS

        elif snakeList[0].x_coordinate == randomItem.x_coordinate and snakeList[
            0].y_coordinate == randomItem.y_coordinate:
            print("You got the item!")
            randomItem.new_item()
            if snakeList[0].direction == "UP":
                x = Snake(snakeList[current_snake].x_coordinate + 1, snakeList[current_snake].y_coordinate)
                x.attr = count
                snakeList.append(x)
                current_snake = current_snake + 1

            if snakeList[0].direction == "DOWN":
                x = Snake(snakeList[current_snake].x_coordinate - 1, snakeList[current_snake].y_coordinate)
                x.attr = count
                snakeList.append(x)
                current_snake = current_snake + 1

            if snakeList[0].direction == "LEFT":
                x = Snake(snakeList[current_snake].x_coordinate, snakeList[current_snake].y_coordinate + 1)
                x.attr = count
                snakeList.append(x)
                current_snake = current_snake + 1

            if snakeList[0].direction == "UP":
                x = Snake(snakeList[current_snake].x_coordinate, snakeList[current_snake].y_coordinate - 1)
                x.attr = count
                snakeList.append(x)
                current_snake = current_snake + 1


    screen.fill(BLACK)

    # This populates the grid with the white squares. and when a row and a column is equal to one,
    # it turns the colour green.

    for row in range(AMOUNT_PER_LINE):
        for column in range(AMOUNT_PER_LINE):
            color = WHITE
            if grid[row][column] == 0:
                color = WHITE
            elif grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED
            pg.draw.rect(screen,
                         color,
                         [(MARGIN + WIDTH) * column + MARGIN,
                          (MARGIN + HEIGHT) * row + MARGIN,
                          WIDTH,
                          HEIGHT])

    clock.tick(60)

    pg.display.flip()

pg.quit()
