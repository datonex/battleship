# Imports
from random import randint
import math
import string

# Variables
grid_size = 9
board = [['.'] * grid_size for i in range(grid_size)]
alphabet_list = list(string.ascii_uppercase)
turn = 0
total_turns = math.floor(grid_size**2/1.25)

# Ship Class

# Draw Board Class for computer and for user

# Functions

def print_board(board_in):
    # Use alphabet to represent columns of game board.
    # https://www.delftstack.com/howto/python/python-alphabet-list/
    print('\n  ' + ' '.join(str(i) for i in list(map(chr, range(65, 65 + grid_size)))))
    for i in range(grid_size):
        print(str(i + 1) + ' ' + ' '.join(str(i) for i in board_in[i]))

def random_row(board_in):
    row = randint(0, len(board_in) - 1)
    return row

def random_col(board_in):
    col = randint(0, len(board_in) - 1)
    return col

def letter_and_index_conversion(value, grid_size):
    alphabet_list = list(string.ascii_uppercase)
    number_list = [i for i in range(1,27)]
    col_dictionary = dict(zip(alphabet_list,number_list))
    
    if type(value) == str and value.upper() in col_dictionary:
        return col_dictionary[value.upper()] # return index
    elif type(value) == int and value > 0 and value <= grid_size:
        letter = list(col_dictionary.keys())[list(col_dictionary.values()).index(value)]
        return letter # return Letter
    else:
        raise ValueError(f'Value entered does not exist in the board.\n Please enter: \n a letter for the column between {alphabet_list[0]} and {alphabet_list[grid_size - 1]} \n a number between 1 and {grid_size} for the row')

print_board(board)
ship_row = random_row(board)
ship_col = random_col(board) - 1

def main():
    for turn in range(grid_size + total_turns):
        print(f'Turn: {turn + 1} of {total_turns}')
        
        # Remove print statement at end of project
        print(letter_and_index_conversion(ship_col, grid_size), ship_row)

        letter_col = str(input(f'Guess a column between {alphabet_list[0]} and {alphabet_list[grid_size - 1]}: \n')).upper()
        guess_col = letter_and_index_conversion(letter_col, grid_size)
        guess_row = int(input(f'Guess a row number between 1 and {grid_size}: \n'))
        print(f'You entered: {letter_col.upper()}{guess_row}')
        if guess_row == ship_row and guess_col == ship_col:
            print('Congratulations Captain! You got a hit!')
            board[guess_row - 1][guess_col - 1] = 'X'
            print_board(board)
        else:
            smallest_col_value = letter_and_index_conversion(alphabet_list[0], grid_size)
            largest_col_value = letter_and_index_conversion(alphabet_list[grid_size - 1], grid_size)
            
            if (guess_row < 1 or guess_row > grid_size) or (guess_col < smallest_col_value or guess_col > largest_col_value):
                print("Bruh! That's not even in the ocean o_O")
            elif board[guess_row - 1][guess_col - 1] == 'X' or board[guess_row - 1][guess_col - 1] == '*':
                print('You guessed this one already -_-')
            else:
                print('Your aim is WAY off!')
                board[guess_row - 1][guess_col - 1] = '*'
                print_board(board)

main()