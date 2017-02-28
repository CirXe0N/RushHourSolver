class GameBoard(object):
    def __init__(self, height, width):
        self.grid = []
        self.height = height
        self.width = width
        self.generate_grid()

    def generate_grid(self):
        """Generate the grid."""
        for row in range(self.height):
            self.grid.append([])
            for column in range(self.width):
                self.grid[row].append(0)

    def get_grid(self):
        """Get the grid."""
        return self.grid

    def add_vehicle(self, vehicle, locations):
        """Add vehicle to the game board."""
        for location in locations:
            x = location['x']
            y = location['y']
            self.grid[x][y] = vehicle

    def get_height(self):
        """Get the height of the game board."""
        return self.height

    def get_width(self):
        """Get the width of the game board."""
        return self.width
