from Game_Data import data
from Higher_Lower_Art import logo
from Higher_Lower_Art import vs
import random
import os


def clearConsole():
    """Clears console when called"""
    return os.system(
        'cls' if os.name in ('nt', 'dos') else 'clear')


def get_random_account():
    """returns a random account from Game_Data"""
    return random.choice(data)


account_a = get_random_account()
account_b = get_random_account()


def formatted_data(account):
    """returns the account as formatted, printable data"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description} from {country}"


def check_answer(guess, num_followers_a, num_followers_b):
    """when guess is correct, returns True, otherwise returns False"""
    if num_followers_a > num_followers_b:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_on = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_on:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {formatted_data(account_a)}")
        print(vs)
        print(f"To B: {formatted_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        num_followers_a = account_a["follower_count"]
        num_followers_b = account_b["follower_count"]
        is_correct = check_answer(guess, num_followers_a, num_followers_b)

        clearConsole()
        print(logo)
        if is_correct:
            score += 1
            print(f"Correct, current score: {score}")
        else:
            game_on = False
            print(f"Incorrect. Your final score: {score}")


game()
