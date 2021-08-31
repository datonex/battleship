# Imports
import random
import math
import string

# Variabless
grid_size = 9
num_ships = 10
board = [["."] * grid_size for i in range(grid_size)]
alphabet_list = list(string.ascii_uppercase)
total_turns = math.floor(grid_size ** 2 / 1.25)


# Functions
def print_board(board_in):
    """
    Function will print board to the display
    """

    # https://www.delftstack.com/howto/python/python-alphabet-list/
    print("\n  " + " ".join(str(i) for i in list(map(chr, range(65, 65 + grid_size)))))
    for i in range(grid_size):
        print(str(i + 1) + " " + " ".join(str(i) for i in board_in[i]))


def random_row(board_in):
    """
    Function will generate a random row index
    """

    row = random.randint(1, len(board_in) - 1)
    return row


def random_col(board_in):
    """
    Function will generate a random column index
    """

    col = random.randint(1, len(board_in) - 1)
    return col


def letter_and_index_conversion(value, grid_size):
    """
    Function will convert all letters to an integer or integer to a capital letter
    """

    number_list = [i for i in range(1, 27)]
    col_dictionary = dict(zip(alphabet_list, number_list))

    if type(value) == str and value.upper() in col_dictionary:
        return col_dictionary[value.upper()]  # return index
    elif type(value) == int and value > 0 and value <= grid_size:
        letter = list(col_dictionary.keys())[list(col_dictionary.values()).index(value)]
        return letter  # return Letter
    else:
        raise ValueError("Invalid value please enter a number or a letter")


def get_row():
    """
    Function will prompt user for input of the row. It will also check if the input is the correct data type and display errors accordingly
    """

    while True:
        try:
            guess = int(input("Guess a row: \n"))
            if guess in range(1, grid_size + 1):
                return guess
            else:
                print("Bruh! That's not even in the ocean o_O")
        except ValueError:
            print(f"\nPlease enter number between 1 and {grid_size}")


def get_col():
    """
    Function will prompt user for input of the column. It will also check if the input is the correct data type and display errors accordingly
    """

    while True:
        try:
            guess_letter = str(input("Guess a column: \n")).upper()
            guess = letter_and_index_conversion(guess_letter, grid_size)
            if guess in range(1, grid_size + 1):
                return guess
            else:
                print("Bruh! That's not even in the ocean o_O")
        except ValueError:
            print(
                f"\nPlease enter a letter for the column between {alphabet_list[0]} and {alphabet_list[grid_size - 1]}"
            )


def game_restart(response):
    """
    Function will prompt user if they want to restart the game. If yes, the board will be reset and the game starts again if not the game will end
    """
    while True:
        # https://stackoverflow.com/questions/7571635/fastest-way-to-check-if-a-value-exists-in-a-list
        yes_set = {"YES", "yes", "y"}
        no_set = {"NO", "no", "n"}
        try:
            if response in yes_set:
                main()
            elif response in no_set:
                print("Thanks for playing :)\n")
                exit()
        except ValueError:
            print('Enter "y" or "n"')


def main():
    """
    Main game function. It will run the game when called
    """

    board = [["."] * grid_size for i in range(grid_size)]
    ship_row = random_row(board)
    ship_col = random_col(board) - 1
    ships = 0
    turn = 0

    print_board(board)
    while turn < total_turns:

        print(letter_and_index_conversion(ship_col, grid_size), ship_row)
        guess_col = get_col()
        guess_row = get_row()

        print("-" * 35)
        print(
            f"You entered: {letter_and_index_conversion(guess_col, grid_size)}{guess_row} \n"
        )

        if guess_row == ship_row and guess_col == ship_col:
            board[guess_row - 1][guess_col - 1] = "X"
            print("Congratulations Captain! You got a hit!")
            print_board(board)
            print("-" * 35)
            turn += 1
            ships += 1
            ship_row = random_row(board)
            ship_col = random_col(board)
            if ships == 10:
                print("Congratulations Captain! You won!")
                game_prompt = input("Restart? y/n: \n")
                game_restart(game_prompt)
        else:
            if (
                board[guess_row - 1][guess_col - 1] == "X"
                or board[guess_row - 1][guess_col - 1] == "*"
            ):
                print("You already guessed this one -_-")
                print("-" * 35)
            else:
                print("Your aim is WAY off! \n")
                board[guess_row - 1][guess_col - 1] = "*"
                print_board(board)
                print("-" * 35)
                turn += 1
                if turn == total_turns:
                    print("Game Over! You ran out of turns")
                    print("-" * 35)
                    game_prompt = input("Restart? y/n: \n")
                    game_restart(game_prompt)

        print(f"Turn {turn + 1} of {total_turns}")
        print(f"You have {10 - ships} ships left")


print("Welcome to battleships!")
print(" * The objective is to sink the enemy's ships")
print(" * Each column is represented by a letter")
print(" * Each row is represented by a number")
print(" * The number of turns will be show after you first turn")
print(" * To win the game you need to find the locations of 10 ships. Good luck!")


def start_game(response):
    """
    Function will prompt user if they want to start the game. If yes, the game will start
    """
    while True:
        yes_set = {"YES", "yes", "y"}
        no_set = {"NO", "no", "n"}
        try:
            if response in yes_set:
                main()
            elif response in no_set:
                print("TOO BAD! WAR WAITS FOR NO ONE!")
                main()
        except ValueError:
            print('Enter "y" or "n"')


game_start = input("Ready? y/n: \n")
start_game(game_start)
# END
