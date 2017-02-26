import datetime
from controllers.board_loader import BoardLoader
from controllers.board_solver import BoardSolver
from enums.direction import Direction
from enums.orientation import Orientation


if __name__ == "__main__":
    # Start Timer
    start_time = datetime.datetime.now()
    loader = BoardLoader('./boards/1.txt')
    game_board = loader.get_game_board()
    solver = BoardSolver(game_board)
    solution = solver.get_solution()

    if solution:
        for index, move in enumerate(solution):
            vehicle = move[0]
            direction = move[1]
            direction_name = ''
            if vehicle.get_orientation() == Orientation.HORIZONTAL and direction == Direction.FORWARD:
                direction_name = 'Right'

            if vehicle.get_orientation() == Orientation.HORIZONTAL and direction == Direction.BACKWARD:
                direction_name = 'Left'

            if vehicle.get_orientation() == Orientation.VERTICAL and direction == Direction.FORWARD:
                direction_name = 'Down'

            if vehicle.get_orientation() == Orientation.VERTICAL and direction == Direction.BACKWARD:
                direction_name = 'Up'

            print('%02d: %s -> %s' % (index + 1, vehicle.get_name(), direction_name))
    else:
        print('This puzzle is even unsolvable for me :(')
    print(start_time, datetime.datetime.now())


