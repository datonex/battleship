# Imports
from random import randint
import string

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

# Remove print statement at end of project
# print(letter_and_index_conversion(ship_col, grid_size), ship_row)
letter_col = str(input("Guess col: ")).upper()
guess_col = letter_and_index_conversion(letter_col, grid_size)
guess_row = int(input("Guess row: "))
print(f'You entered position: {letter_col.upper()}{guess_row}')

if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations Captain! You got a hit!")
    board[guess_col][guess_row] = 'O'
    print_board(board)
else: 
    print("Your aim is WAY off!")
    board[guess_col][guess_row] = 'X'
    print_board(board)