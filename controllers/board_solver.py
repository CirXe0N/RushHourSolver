import threading
from copy import deepcopy
from enums.direction import Direction
from enums.orientation import Orientation


class BoardSolver(object):
    def __init__(self, game_board, console_view):
        self.game_board = game_board
        self.console_view = console_view
        self.solution = None

    def get_solution(self):
        """Find the solution of the game board"""
        grid = self.game_board.get_grid()
        visited = set()
        queue = [[[], grid]]

        while len(queue) > 0:
            threads = []
            moves = []
            for item in range(len(queue)):
                moves, grid = queue.pop(0)

                self.console_view.display_grid(grid, self.game_board.get_height(), self.game_board.get_width())

                if self.is_solved(grid):
                    return moves

                threads.append(SolverThread(grid, self.game_board.get_height(), self.game_board.get_width()))

            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join()

            for thread in threads:
                for new_moves, new_grid in thread.states:
                    if hash(str(new_grid)) not in visited:
                        queue.append([moves + new_moves, new_grid])
                        visited.add(hash(str(new_grid)))
        return None

    def is_solved(self, grid):
        """Check if game board is solved."""
        for row in range(self.game_board.get_height()):
            for column in range(self.game_board.get_width()):
                vehicle = grid[column][row]

                if vehicle and vehicle.is_main_vehicle() and column == self.game_board.get_width() - 1:
                    return True
        return False


class SolverThread(threading.Thread):
    def __init__(self, grid, width, height):
        self.grid = grid
        self.height = height
        self.width = width
        self.states = []
        threading.Thread.__init__(self)

    def run(self):
        """Run the breadth first search algorithm to find the solution."""
        for row in range(self.height):
            for column in range(self.width):
                vehicle = self.grid[column][row]
                if vehicle:
                    for direction in Direction:
                        if self.is_movable(vehicle, direction, self.grid):
                            new_grid = deepcopy(self.grid)
                            new_vehicle = new_grid[column][row]

                            if direction == Direction.BACKWARD:
                                new_vehicle.move_backward()

                            if direction == Direction.FORWARD:
                                new_vehicle.move_forward()

                            old_locations = vehicle.get_occupied_locations()
                            new_locations = new_vehicle.get_occupied_locations()
                            new_grid = self.update_vehicle(new_grid, new_vehicle, old_locations, new_locations)
                            self.states.append([[[vehicle, direction]], new_grid])
        return self.states

    def is_movable(self, vehicle, direction, grid):
        """Check if vehicle object is movable to the next empty space."""
        if vehicle.get_orientation() == Orientation.HORIZONTAL and direction == Direction.FORWARD:
            location = vehicle.get_end_location()
            x = location['x'] + 1
            y = location['y']

            if x < self.width:
                board_vehicle = grid[x][y]
                if board_vehicle:
                    return False
            else:
                return False

        if vehicle.get_orientation() == Orientation.HORIZONTAL and direction == Direction.BACKWARD:
            location = vehicle.get_start_location()
            x = location['x'] - 1
            y = location['y']

            if x > -1:
                board_vehicle = grid[x][y]
                if board_vehicle:
                    return False
            else:
                return False

        if vehicle.get_orientation() == Orientation.VERTICAL and direction == Direction.FORWARD:
            location = vehicle.get_end_location()
            x = location['x']
            y = location['y'] + 1

            if y < self.height:
                board_vehicle = grid[x][y]
                if board_vehicle:
                    return False
            else:
                return False

        if vehicle.get_orientation() == Orientation.VERTICAL and direction == Direction.BACKWARD:
            location = vehicle.get_start_location()
            x = location['x']
            y = location['y'] - 1

            if y > -1:
                board_vehicle = grid[x][y]
                if board_vehicle:
                    return False
            else:
                return False

        return True

    @staticmethod
    def update_vehicle(grid, vehicle, old_locations, new_locations):
        """Update grid with the vehicles' new location."""
        for location in old_locations:
            x = location['x']
            y = location['y']
            grid[x][y] = 0

        for location in new_locations:
            x = location['x']
            y = location['y']
            grid[x][y] = vehicle

        return grid
