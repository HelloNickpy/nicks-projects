""" Number Guessing Game
----------------------------------------
"""
import random

attempts_list = []


def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, lets change that!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))


def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello there! Welcome to the Number Guessing Game!")
    player_name = input("What is your name?: ")
    wanna_play = input("Hello {}! Would you like to play the guessing game?? (Enter Yes/No): ".format(player_name))
    # Where the show_score function USED to be
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10: ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range: ")
            if int(guess) == random_number:
                print("Awesome! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("Understood, have a good one!")
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("Understood, have a good one!")


if __name__ == '__main__':
    start_game()
