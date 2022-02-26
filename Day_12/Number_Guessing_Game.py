
import random
from Number_game_art import logo

EASY_NUM_ATTEMPTS = 10
HARD_NUM_ATTEMPTS = 5


def check_guess(guess, num_to_guess, number_of_attempts):
    """Checks the guess, and return the number of attempts left."""
    if guess > num_to_guess:
        print("Too high.")
        return number_of_attempts - 1
    elif guess < num_to_guess:
        print("Too low.")
        return number_of_attempts - 1
    else:
        print(f"You guessed correctly! The right answer was {num_to_guess}")


def set_difficulty():
    """Returns the number of attempts corresponding to the chosen difficulty level."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_NUM_ATTEMPTS
    elif level == "hard":
        return HARD_NUM_ATTEMPTS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100.")
    num_to_guess = random.randint(1, 100)

    number_of_attempts = set_difficulty()
    guess = 0
    while guess != num_to_guess:
        guess = int(
            input(f"You have {number_of_attempts} attempts remaining.\nMake a guess: "))

        number_of_attempts = check_guess(
            guess, num_to_guess, number_of_attempts)
        if number_of_attempts == 0:
            print("You've run out of guesses, you lose.")
            return  # ends the function/game
        elif guess != num_to_guess:
            print("Guess again.\n")


game()
