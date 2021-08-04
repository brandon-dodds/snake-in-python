from src.Colours import Colours


class GridLogic:
    # Defining colour constants
    HEIGHT = 16
    WIDTH = 16
    MARGIN = 3
    AMOUNT_PER_LINE = 16

    grid = []  # This is the grid 2d array.

    def __init__(self):

        for row in range(self.AMOUNT_PER_LINE):  # You can change these values for bigger map size.
            self.grid.append([])
            for column in range(self.AMOUNT_PER_LINE):
                self.grid[row].append(Colours.WHITE)  # Creates a 2d array which my grid will be based.

    def make_white(self, x_coordinate, y_coordinate):
        self.grid[x_coordinate][y_coordinate] = Colours.WHITE

    def make_green(self, x_coordinate, y_coordinate):
        self.grid[x_coordinate][y_coordinate] = Colours.GREEN
