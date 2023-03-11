"""
This imports the necessary modules random, time, and colorama

Initializes the colorama module.
"""
import random
import time
from colorama import init, Fore, Style

init()


# Class for determining the selection of a shape
class SelectShapeOfFigure:
    variable = {1: 'rock', 2: 'paper', 3: 'scissors'}

    def __init__(self):
        self.computer_choice_shape = None
        self.user_choice_shape = None

    def computer_choice(self):
        """
        Definition of the computer_choice method generates a random integer from 1 to 3
        :return: uses it to set a random withdrawal representing: rock, paper, or scissors.
        """
        random_selection = random.randint(1, 3)
        self.computer_choice_shape = SelectShapeOfFigure.variable[random_selection]

    def user_choice(self):
        while True:
            self.user_choice_shape = input("Choose one of the shapes (rock/paper/scissors): ").lower()
            if self.user_choice_shape not in ('rock', 'paper', 'scissors'):
                print('Incorrect input. Please try again')
                continue
            break


# Subclass to determine the winner of the game
class WhoWinner(SelectShapeOfFigure):

    def game_winner(self):
        """
        game_winner method that simulates the rock-paper-scissors game
        it calls the computer_choice and user_choice methods to get the shapes chosen by each player
            - prints out the available choices
            - determines the winner
            - updates the score
            - prints the current score after each round.
        The Python package `colorama` provides for the producing colored terminal text, which increases readability.
        Once one player scores 3 points:
        :return: prints the appropriate message to declare the winner.
        """
        player_points = 0
        computer_points = 0
        while player_points < 3 and computer_points < 3:
            self.computer_choice()
            self.user_choice()

            for i in SelectShapeOfFigure.variable.values():
                # Start the count by saying the name of the game
                print(Fore.WHITE + "\t" + i.upper(), end='... ')
                time.sleep(0.4)
            print()

            if self.computer_choice_shape == self.user_choice_shape:
                print(Fore.CYAN + "Draw")
            elif (self.user_choice_shape == 'rock' and self.computer_choice_shape == "scissors"
                  or self.user_choice_shape == "paper" and self.computer_choice_shape == "rock"
                  or self.user_choice_shape == "scissors" and self.computer_choice_shape == "paper"):
                print(Fore.CYAN + "Your point")
                player_points += 1
            else:
                print(Fore.CYAN + "The computer's point")
                computer_points += 1
            print(Fore.YELLOW + f'\t User - {player_points}  /  Computer - {computer_points}' + Style.RESET_ALL)

        if player_points == 3:
            print("Congratulations, Player. You have Won!")
        else:
            print("Unfortunately, today fortune was not on your side. The Computer Won!")


if __name__ == '__main__':
    result = WhoWinner()
    result.game_winner()
