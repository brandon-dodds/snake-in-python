import Colours


class Grid:
    MARGIN = 3
    AMOUNT_PER_LINE = 16

    grid = []

    def __init__(self):

        for row in range(self.AMOUNT_PER_LINE):
            self.grid.append([])
            for column in range(self.AMOUNT_PER_LINE):
                self.grid[row].append(Colours.WHITE)

    def make_colour(self, x_coordinate, y_coordinate, colour):
        self.grid[x_coordinate][y_coordinate] = colour
