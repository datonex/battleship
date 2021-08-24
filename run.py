# Imports
from random import randint
# Variables
grid_size = 9
board = [['.'] * grid_size for i in range(grid_size)]

# Ship Class

# Draw Board Class for computer and for user

# Functions

def print_board(board_in):
    # Use alphabet to represent columns of game board.
    # https://www.delftstack.com/howto/python/python-alphabet-list/
    print("\n  " + " ".join(str(i) for i in list(map(chr, range(65, 65 + grid_size)))))
    for i in range(grid_size):
        print(str(i + 1) + " " + " ".join(str(i) for i in board_in[i]))

def random_row(board_in):
    row = randint(0, len(board_in) - 1)
    return row

def random_col(board_in):
    col = randint(0, len(board_in) - 1)
    return col

print_board(board)
ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row, ship_col)
guess_col = (input("Guess col: "))
guess_row = int(input("Guess row: "))
print(f'You entered position: {guess_col}{guess_row}')
