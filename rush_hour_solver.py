from controllers.board_loader import BoardLoader
from controllers.board_solver import BoardSolver

if __name__ == "__main__":
    loader = BoardLoader('./boards/board1.txt')
    game_board = loader.get_game_board()

    solver = BoardSolver(game_board)
    solution = solver.get_solution()

    print(solution)

    # for index, step in solution:
    #     print('%s: %s' % (index, step))
