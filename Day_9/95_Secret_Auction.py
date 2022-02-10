
# !! from replit import clear !!
import os
from Secret_Auction_art import logo
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
#HINT: You can call clear() to clear the output in the console.

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of € {highest_bid}")

while not bidding_finished:
    name = input("What is your name? ")
    price = float(input("What's your bid? € "))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no':\n").lower()
    if should_continue == "no":
        bidding_finished = True
        clearConsole()
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clearConsole()
