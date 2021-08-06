import Colours


class Grid:
    HEIGHT = 16
    WIDTH = 16
    MARGIN = 3
    AMOUNT_PER_LINE = 16

    grid = []

    def __init__(self):

        for row in range(self.AMOUNT_PER_LINE):
            self.grid.append([])
            for column in range(self.AMOUNT_PER_LINE):
                self.grid[row].append(Colours.WHITE)

    def make_white(self, x_coordinate, y_coordinate):
        self.grid[x_coordinate][y_coordinate] = Colours.WHITE

    def make_green(self, x_coordinate, y_coordinate):
        self.grid[x_coordinate][y_coordinate] = Colours.GREEN
