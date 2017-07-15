from collections import deque
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

grid = [] # This is the grid 2d array.
for row in range(AMOUNT_PER_LINE): # You can change these values for bigger map size.
    grid.append([])
    for column in range(AMOUNT_PER_LINE):
        grid[row].append(0)  # Creates a 2d array which my grid will be based.


# Creating the snakeList object.

class Snake:
    x_coordinate = 0 # These are the X and Y coordinates stored for each snake.
    y_coordinate = 0
    direction = "UP" # This is the direction the snake is going.

    def __init__(self, x_coordinate, y_coordinate): # This is executed when a snake is created.
        grid[x_coordinate][y_coordinate] = 1 # The place where it is created is '1' means that the block is green.
        self.x_coordinate = x_coordinate # The X and Y coordinates become the new X and Y coordinates.
        self.y_coordinate = y_coordinate

    def make_white(self):
        grid[self.x_coordinate][self.y_coordinate] = 0

    def make_green(self, direction):

        if direction == "UP":
            grid[self.x_coordinate - 1][self.y_coordinate] = 1
            self.x_coordinate = self.x_coordinate - 1
            self.direction = "UP"

        elif direction == "DOWN":
            grid[self.x_coordinate + 1][self.y_coordinate] = 1
            self.x_coordinate = self.x_coordinate + 1
            self.direction = "DOWN"

        elif direction == "LEFT":
            grid[self.x_coordinate][self.y_coordinate - 1] = 1
            self.y_coordinate = self.y_coordinate - 1
            self.direction = "LEFT"

        elif direction == "RIGHT":
            grid[self.x_coordinate][self.y_coordinate + 1] = 1
            self.y_coordinate = self.y_coordinate + 1
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
        self.x_coordinate = random.randint(1, 15)
        self.y_coordinate = random.randint(1, 15)
        for x in range(len(snakeList)):
            if self.x_coordinate and self.y_coordinate == snakeList[x].x_coordinate and snakeList[x].y_coordinate:
                self.new_item()

        grid[self.x_coordinate][self.y_coordinate] = 2


# Defining the new move function

# TODO implement my buffer design.

movementList = deque([])
def move(direction):
    movementList.appendleft(direction)
    for x in range(len(snakeList)):
        snakeList[x].make_white()
    for x in range(len(snakeList)):
        snakeList[x].make_green(movementList[x])


# Beginning pygame.
pg.init()

# The size of the window that will be a constant. Edit if you want the window size to be bigger.

WINDOW_SIZE = [308, 308]

screen = pg.display.set_mode(WINDOW_SIZE)

pg.display.set_caption("Snake Game")

# Important variables and declaration of objects.
current_snake = 0
score = 0
snakeList = []
x = Snake(8, 8)
snakeList.append(x)
randomItem = RandomObject()
done = False
clock = pg.time.Clock()

while not done:

    for event in pg.event.get():
        # QUITTING THE PROGRAM.
        if event.type == pg.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        # USER INPUT
        elif pg.key.get_pressed()[pg.K_q] != 0:
            done = True

        elif pg.key.get_pressed()[pg.K_w] or pg.key.get_pressed()[pg.K_UP]:
            move("UP")

        elif pg.key.get_pressed()[pg.K_s] or pg.key.get_pressed()[pg.K_DOWN]:
            move("DOWN")

        elif pg.key.get_pressed()[pg.K_a] or pg.key.get_pressed()[pg.K_LEFT]:
            move("LEFT")

        elif pg.key.get_pressed()[pg.K_d] or pg.key.get_pressed()[pg.K_RIGHT]:
            move("RIGHT")

        # CONTROL STATEMENTS

        if snakeList[0].x_coordinate == randomItem.x_coordinate and \
                snakeList[0].y_coordinate == randomItem.y_coordinate:
            print("You got the item!")
            score += 10
            print(score)
            randomItem.new_item()

            if snakeList[current_snake].direction == "UP":
                x = Snake(snakeList[current_snake].x_coordinate + 1, snakeList[current_snake].y_coordinate)

            elif snakeList[current_snake].direction == "DOWN":
                x = Snake(snakeList[current_snake].x_coordinate - 1, snakeList[current_snake].y_coordinate)

            elif snakeList[current_snake].direction == "LEFT":
                x = Snake(snakeList[current_snake].x_coordinate, snakeList[current_snake].y_coordinate + 1)

            elif snakeList[current_snake].direction == "RIGHT":
                x = Snake(snakeList[current_snake].x_coordinate, snakeList[current_snake].y_coordinate - 1)

            snakeList.append(x)
            current_snake += 1

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