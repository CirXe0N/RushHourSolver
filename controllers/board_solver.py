from copy import deepcopy
from queue import Queue
from enums.direction import Direction
from enums.orientation import Orientation


class BoardSolver(object):
    def __init__(self, game_board):
        self.game_board = game_board
        self.solution = None

    def get_solution(self):
        grid = self.game_board.get_grid()
        visited = set()
        queue = Queue()
        queue.put([[], grid])

        while not queue.empty():
            moves, grid = queue.get()

            self.print_grid(grid)

            if self.is_solved(grid):
                return moves

            for new_moves, new_grid in self.get_states(grid):
                if hash(str(new_grid)) not in visited:
                    queue.put([moves + new_moves, new_grid])
                    visited.add(hash(str(new_grid)))

        return None

    def print_grid(self, grid):
        print('----------------------')
        for row in range(self.game_board.get_height()):
            for column in range(self.game_board.get_width()):
                vehicle = grid[column][row]
                if vehicle:
                    print(vehicle.get_name(), end=' ')
                else:
                    print('.', end=' ')

                if column == self.game_board.get_width() - 1:
                    print('')
        print('----------------------')

    def get_states(self, grid):
        states = []
        for row in range(self.game_board.get_height()):
            for column in range(self.game_board.get_width()):
                vehicle = grid[column][row]
                if vehicle:
                    for direction in Direction:
                        if self.is_movable(vehicle, direction, grid):
                            new_grid = deepcopy(grid)
                            new_vehicle = new_grid[column][row]

                            if direction == Direction.BACKWARD:
                                new_vehicle.move_backward()

                            if direction == Direction.FORWARD:
                                new_vehicle.move_forward()

                            old_locations = vehicle.get_occupied_locations()
                            new_locations = new_vehicle.get_occupied_locations()
                            new_grid = self.update_vehicle(new_grid, new_vehicle, old_locations, new_locations)
                            states.append([[[vehicle, direction]], new_grid])
        return states

    def update_vehicle(self, grid, vehicle, old_locations, new_locations):
        for location in old_locations:
            x = location['x']
            y = location['y']
            grid[x][y] = 0

        for location in new_locations:
            x = location['x']
            y = location['y']
            grid[x][y] = vehicle

        return grid

    def is_movable(self, vehicle, direction, grid):
        if vehicle.get_orientation() == Orientation.HORIZONTAL and direction == Direction.FORWARD:
            location = vehicle.get_end_location()
            x = location['x'] + 1
            y = location['y']

            if x < self.game_board.get_width():
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

            if y < self.game_board.get_height():
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

    def is_solved(self, grid):
        for row in range(self.game_board.get_height()):
            for column in range(self.game_board.get_width()):
                vehicle = grid[column][row]

                if vehicle and vehicle.is_main_vehicle() and column == self.game_board.get_width() - 1:
                    print(vehicle)
                    return True
        return False
