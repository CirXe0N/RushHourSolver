from copy import deepcopy
from enums.direction import Direction
from enums.orientation import Orientation


class BoardSolver(object):
    def __init__(self, game_board):
        self.solution = None
        self.game_board = game_board

    def get_solution(self):
        steps = []
        visited = []
        queue = [self.game_board.get_vehicles()]

        while len(queue) != 0:
            vehicles = queue.pop(0)

            if self.is_solved(vehicles):
                return steps

            snapshots = self.create_snapshots(vehicles)

            for snapshot in snapshots:
                if hash(str(snapshot)) not in visited:
                    queue.append(snapshot)
                    visited.append(hash(str(snapshot)))
        return None

    def create_snapshots(self, vehicles):
        snapshots = []

        for vehicle in vehicles:
            for direction in Direction:
                if self.is_movable(vehicle, direction, vehicles):
                    new_vehicles = deepcopy(vehicles)
                    new_vehicle = list(filter(lambda x: x.name == vehicle.name, new_vehicles))[0]
                    if direction == Direction.BACKWARD:
                        new_vehicle.move_backward()

                    if direction == Direction.FORWARD:
                        new_vehicle.move_forward()

                    print(new_vehicle.name, new_vehicle.get_start_location(), new_vehicle.get_end_location(), direction)

                    snapshots.append(new_vehicles)
        return snapshots

    def is_movable(self, vehicle, direction, vehicles):
        start_location = vehicle.get_start_location()
        end_location = vehicle.get_end_location()

        for board_vehicle in vehicles:
            occupied_locations = board_vehicle.get_occupied_locations()

            if vehicle.get_orientation() == Orientation.HORIZONTAL and direction == Direction.FORWARD:
                next_location = {
                    'x': end_location['x'] + 1,
                    'y': end_location['y']
                }

                if next_location['x'] >= self.game_board.get_width() or next_location in occupied_locations:
                    return False

            if vehicle.get_orientation() == Orientation.VERTICAL and direction == Direction.FORWARD:
                next_location = {
                    'x': end_location['x'],
                    'y': end_location['y'] + 1
                }

                if next_location['y'] >= self.game_board.get_height() or next_location in occupied_locations:
                    return False

            if vehicle.get_orientation() == Orientation.HORIZONTAL and direction == Direction.BACKWARD:
                next_location = {
                    'x': start_location['x'] - 1,
                    'y': start_location['y']
                }

                if next_location['x'] < 0 or next_location in occupied_locations:
                    return False

            if vehicle.get_orientation() == Orientation.VERTICAL and direction == Direction.BACKWARD:
                next_location = {
                    'x': start_location['x'],
                    'y': start_location['y'] - 1
                }

                if next_location['y'] < 0 or next_location in occupied_locations:
                    return False
        return True

    def is_solved(self, vehicles):
        main_vehicle = None
        for vehicle in vehicles:
            if vehicle.is_main_vehicle():
                main_vehicle = vehicle

        if main_vehicle and main_vehicle.get_end_location()['x'] == self.game_board.get_width() - 1:
            return True
        return False
