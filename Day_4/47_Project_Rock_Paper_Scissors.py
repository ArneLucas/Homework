rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to Rock, Paper, Sciccors!")

games_images = [rock, paper, scissors]

player_pick = int(input("Do you play [1] Rock [2] Paper or [3] Scissors?\n"))
player_pick_index = player_pick -1

if player_pick > 3 or player_pick <= 0:
    print("You filled in an invalid number, try again")
else:
    computer_pick = random.randint(1,3)
    computer_pick_index = computer_pick -1

    print(f"You picked:\n {games_images[player_pick_index]}")
    print(f"Computer picked:\n {games_images[computer_pick_index]}")

    if player_pick == 1 and computer_pick == 3:
        print("You win!")
    elif player_pick == 3 and computer_pick == 1:
        print("You lose!")
    elif player_pick < computer_pick:
        print("You lose!")
    elif player_pick > computer_pick:
        print("You win!")
    elif player_pick == computer_pick:
        print("It's a draw, try again")