from sys import exit, modules

instructions = f"""
These are the numerical positions of our elements on the board
     1 | 2 | 3
    ---|---|---
     4 | 5 | 6 
    ---|---|---
     7 | 8 | 9
"""

game_board = []
position_sheet = []

for i in range(9):
    game_board.append(' ')


def print_board(game_board):
    filled_board = f"""
        {game_board[0]} | {game_board[1]} | {game_board[2]}
       ---|---|---
        {game_board[3]} | {game_board[4]} | {game_board[5]}
       ---|---|---
        {game_board[6]} | {game_board[7]} | {game_board[8]}
        """
    print(filled_board)


def input_position(player_name):
    while True:
        try:
            x = int(input(f'{player_name.capitalize()}, your turn: '))
            # make index position
            x -= 1
        except ValueError:
            print("The value can Only be a number in the range 1-9")
            continue
        if 0 <= x < 9:
            if x in position_sheet:
                print("This cell is already occupied, try again")
                continue
            position_sheet.append(x)
            return x
        else:
            print("Table 3х3 doesn't have such a cell number, try again")
        print("Please enter the number only in the range 1-9")


def result_calculation(game_board, player_one, player_two, position_sheet=None):
    if game_board[0] == game_board[1] == game_board[2] == 'X' or game_board[1] == game_board[4] == game_board[
        7] == 'X' or game_board[0] == game_board[4] == game_board[8] == 'X' or game_board[2] == game_board[5] == \
            game_board[8] == 'X' or game_board[3] == game_board[4] == game_board[5] == 'X' or game_board[2] == \
            game_board[4] == game_board[6] == 'X' or game_board[6] == game_board[7] == game_board[8] == 'X' or \
            game_board[0] == game_board[3] == game_board[6] == 'X':
        print(f"Congrats, {player_one}. You've won.")
        if 'ipykernel' in modules:
            exit('Thanks for playing')  # Running inside Jupyter Notebook
        else:
            quit('Thanks for playing')  # Running in a regular Python environment
    elif game_board[0] == game_board[1] == game_board[2] == 'O' or game_board[1] == game_board[4] == game_board[
        7] == 'O' or game_board[0] == game_board[4] == game_board[8] == 'O' or game_board[2] == game_board[5] == \
            game_board[8] == 'O' or game_board[3] == game_board[4] == game_board[5] == 'O' or game_board[2] == \
            game_board[4] == game_board[6] == 'O' or game_board[6] == game_board[7] == game_board[8] == 'O' or \
            game_board[0] == game_board[3] == game_board[6] == 'O':
        print(f"Congrats, {player_two}. You've won.")
        if 'ipykernel' in modules:
            exit('Thanks for playing')  # Running inside Jupyter Notebook
        else:
            quit('Thanks for playing')  # Running in a regular Python environment


def main():
    player_one = input("Enter the first player's name: ")
    player_two = input("Enter the second player's name: ")
    print(instructions)
    print(f"Player {player_one}'s, your symbol -> X")
    print(f"Player {player_two}'s, your symbol -> O")
    input("If you have read the instructions, press 'Enter' ")
    print_board(game_board)
    for game_iteration in range(0, 9):
        if game_iteration % 2 == 0:
            index = input_position(player_one)
            game_board[index] = 'X'
        else:
            index = input_position(player_two)
            game_board[index] = 'O'

        print_board(game_board)
        result_calculation(game_board, player_one, player_two)
    print(f"The players {player_one} and {player_two} played a draw.")


main()
