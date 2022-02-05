import random
from Hangman_art import logo, stages
from Hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False
guessed_letters = []

print(logo)

#Create blanks
display = []
for letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")

# Play
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}")
    # Guessed right
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Guessed wrong
    if guess not in chosen_word:
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

    # Display niceprint
    print(f"{' '.join(display)}")

    # Win check
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Print gallow
    print(stages[lives])