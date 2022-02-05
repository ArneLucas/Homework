#Step 5

import random
from Hangman_art import logo, stages
from Hangman_words import word_list

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False
guessed_letters = []

# Welcome
print(logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in display:
        print(f"You already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in guessed_letters:
            lives -= 1
            guessed_letters.append(guess)
            if lives == 0:
                end_of_game = True
                print("You a dead man!")
            else:
                print(f"Letter {guess} is not in this word. You lose a life")
        else:
            print(f"You already tried letter {guess}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])