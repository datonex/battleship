# Imports
from random import randint
import math
import string


# Variables
grid_size = 9
board = [['.'] * grid_size for i in range(grid_size)]
alphabet_list = list(string.ascii_uppercase)
turn = 0
total_turns = 2
# total_turns = math.floor(grid_size**2/1.25)

# Ship Class

# Draw Board Class for computer and for user

# Functions


def print_board(board_in):
    # Use alphabet to represent columns of game board.
    # https://www.delftstack.com/howto/python/python-alphabet-list/
    print('\n  ' + ' '.join(str(i)
          for i in list(map(chr, range(65, 65 + grid_size)))))
    for i in range(grid_size):
        print(str(i + 1) + ' ' + ' '.join(str(i) for i in board_in[i]))


def random_row(board_in):
    row = randint(1, len(board_in) - 1)
    return row


def random_col(board_in):
    col = randint(1, len(board_in) - 1)
    return col


def letter_and_index_conversion(value, grid_size):
    number_list = [i for i in range(1, 27)]
    col_dictionary = dict(zip(alphabet_list, number_list))

    if type(value) == str and value.upper() in col_dictionary:
        return col_dictionary[value.upper()]  # return index
    elif type(value) == int and value > 0 and value <= grid_size:
        letter = list(col_dictionary.keys())[
            list(col_dictionary.values()).index(value)]
        return letter  # return Letter
    else:
        raise ValueError('Invalid value please enter a number or a letter')


def get_row():
    while True:
        try:
            guess = int(
                input(f'Guess a row: \n'))
            if guess in range(1, grid_size + 1):
                return guess
            else:
                print("Bruh! That's not even in the ocean o_O")
        except ValueError:
            print(f'\nPlease enter number between 1 and {grid_size}')


def get_col():
    while True:
        try:
            guess_letter = str(input(
                f'Guess a column: \n')).upper()
            guess = letter_and_index_conversion(guess_letter, grid_size)
            if guess in range(1, grid_size + 1):
                return guess
            else:
                print("Bruh! That's not even in the ocean o_O")
        except ValueError:
            print(
                f'\nPlease enter a letter for the column between {alphabet_list[0]} and {alphabet_list[grid_size - 1]}')


print_board(board)
ship_row = random_row(board)
ship_col = random_col(board) - 1


def main():
    for turn in range(total_turns):
        print('Turn', turn + 1, 'of', total_turns)

        # Remove print statement at end of project
        print(letter_and_index_conversion(ship_col, grid_size), ship_row)

        guess_col = get_col()
        guess_row = get_row()

        print(
            f'You entered: {letter_and_index_conversion(guess_col, grid_size)}{guess_row}')

        if guess_row == ship_row and guess_col == ship_col:
            board[guess_row][guess_col] = 'X'
            print_board(board)
            print('Congratulations Captain! You got a hit!')
        else:
            smallest_col_value = letter_and_index_conversion(
                alphabet_list[0], grid_size)
            largest_col_value = letter_and_index_conversion(
                alphabet_list[grid_size - 1], grid_size)

            # if (guess_row < 1 or guess_row > grid_size) or (guess_col < smallest_col_value or guess_col > largest_col_value):
            #    print("Bruh! That's not even in the ocean o_O")
            if board[guess_row - 1][guess_col - 1] == 'X' or board[guess_row - 1][guess_col - 1] == '*':
                print('You guessed this one already -_-')
            else:
                print('Your aim is WAY off!')
                board[guess_row - 1][guess_col - 1] = '*'
                if turn == total_turns:
                    print('Game Over! You ran out of turns')
                print_board(board)


main()

# END
