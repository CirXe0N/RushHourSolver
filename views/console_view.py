import curses
import math
from enums.direction import Direction
from enums.orientation import Orientation


class ConsoleView(object):

    def __init__(self):
        self.stdscr = curses.initscr()
        self.stdscr.scrollok(1)
        self.stdscr.idlok(1)
        self.stdscr.syncok(1)
        curses.setupterm()

    def display_loaded_grid(self, grid, height, width):
        # Display game board
        self.display_grid(grid, height, width)

        # Wait for user input
        self.stdscr.addstr('\n')
        self.stdscr.addstr('\n')
        self.stdscr.addstr('Press any key to find solution. \n')
        self.stdscr.getch()

    def display_grid(self, grid, height, width):
        # Clear screen
        self.stdscr.clear()

        # Display game board
        self.stdscr.addstr('The Puzzle: \n', curses.A_BOLD)
        self.stdscr.addstr('\n')
        for row in range(height):
            for column in range(width):
                vehicle = grid[column][row]
                if vehicle:
                    self.stdscr.addstr('%s ' % vehicle.get_name())
                else:
                    self.stdscr.addstr('. ')

                if column == width - 1:
                    self.stdscr.addstr('\n')
        self.stdscr.refresh()

    def display_statistics(self, amount_moves='--', time_delta='--'):
        self.stdscr.addstr('\n')
        self.stdscr.addstr('\n')
        self.stdscr.addstr('The Statistics: \n', curses.A_BOLD)
        self.stdscr.addstr('\n')

        self.stdscr.addstr('Amount of Moves: %s \n' % amount_moves)
        self.stdscr.addstr('Time Passed: %.3f seconds\n' % time_delta)

    def display_solution(self, solution):
        self.stdscr.addstr('\n')
        self.stdscr.addstr('\n')

        if solution:
            # Convert moves to a user friendly format and display them
            self.stdscr.addstr('The Solution: \n', curses.A_BOLD)
            self.stdscr.addstr('\n')

            solution_size = len(solution)
            items_per_row = math.ceil(solution_size / 4)
            for row_index in range(items_per_row):
                collection = []
                for index in range(4):
                    limit = (index * (items_per_row + 1)) + row_index
                    if limit < solution_size:
                        collection.append(limit)

                for column_index, move in enumerate(solution[i] for i in collection):
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

                    display_text = '%02d: %s -> %s ' % (collection[column_index] + 1, vehicle.get_name(),
                                                        direction_name)
                    self.stdscr.addstr(display_text)
                    self.stdscr.addstr(' ' * (20 - len(display_text)))

                    if column_index == len(collection) - 1:
                        self.stdscr.addstr('\n')
                    self.stdscr.refresh()
        else:
            self.stdscr.addstr('This puzzle is unsolvable. Even for me! :( \n')
            self.stdscr.refresh()

    def display_exit_message(self):
        self.stdscr.addstr('\n')
        self.stdscr.addstr('\n')
        self.stdscr.addstr('Thank you for using the rush hour solver. \n')
        self.stdscr.addstr('Press any key to exit. \n')
        self.stdscr.getch()
        curses.endwin()

    def load_board_prompt(self):
        # Clear screen
        self.stdscr.clear()

        # Ask user which game board load
        self.stdscr.addstr('Which board do you want to solve? (filename without extension ".txt") \n')
        self.stdscr.addstr('Make sure the board file is in the directory "boards". \n')
        self.stdscr.addstr('\n')
        self.stdscr.addstr('Filename ', curses.A_BOLD)
        self.stdscr.addstr('(excl. extension ".txt"): ')
        self.stdscr.refresh()
        curses.echo()
        return self.stdscr.getstr(50).decode()
