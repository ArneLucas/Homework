from blackjack_art import logo
import random
import os


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealt_card = random.choice(cards)
    return dealt_card


def calculate_score(hand_of_cards):
    """Takes a hand of cards and calculates the score. If score > 21 and there's an ace, then the ace is not worth 11, but 1 point"""
    if sum(hand_of_cards) == 21 and len(hand_of_cards) == 2:
        return 0
    if 11 in hand_of_cards and sum(hand_of_cards) > 21:
        hand_of_cards.remove(11)
        hand_of_cards.append(1)
    return sum(hand_of_cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Same score, it's a draw \n"
    elif computer_score == 0:
        return "Dealer has Blackjack, you lose \n"
    elif user_score == 0:
        return "Blackjack! You win \n"
    elif user_score > 21:
        return "You went over 21, you lose \n"
    elif computer_score > 21:
        return "Dealer went over 21, you win \n"
    elif user_score > computer_score:
        return "Dealer scored lower, you win \n"
    else:
        return "Dealer scores higher, you lose \n"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal_for_user = input(
                "Type 'y' to hit, type 'n' to stand: ").lower()
            if deal_for_user == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}. Your score: {user_score}")
    print(
        f"\nDealer's final hand: {computer_cards}. Dealer's final score: {computer_score}\n")
    print(compare(user_score, computer_score))

    restart = input("Do you want to play again? y/n: ").lower()
    if restart == "y":
        clearConsole()
        play_game()


play_game()
