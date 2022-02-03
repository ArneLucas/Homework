#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# get N random values from letters, then N random values from numbers, then N random values from symbols (and store them in easy_pass):

easy_pass = ("")

for letter in range(0,nr_letters):
    easy_pass += letters[random.randint(0,(len(letters)-1))]

for symbol in range(0,nr_symbols):
    easy_pass += symbols[random.randint(0,(len(symbols)-1))]

for number in range(0,nr_numbers):
    easy_pass += numbers[random.randint(0,(len(numbers)-1))]
    
print(f"Here's your randomly created easy password: {easy_pass}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# get N random values from letters, then N random values from numbers, then N random values from symbols (and shake 'm and store them in hard_pass_randomized):
hard_pass = ("")

for letter in range(0,nr_letters):
    hard_pass += letters[random.randint(0,(len(letters)-1))]

for symbol in range(0,nr_symbols):
    hard_pass += symbols[random.randint(0,(len(symbols)-1))]

for number in range(0,nr_numbers):
    hard_pass += numbers[random.randint(0,(len(numbers)-1))]

hard_pass_randomized = "".join(random.sample(hard_pass,len(hard_pass)))

print(f"Here's your randomly created hard password: {hard_pass_randomized}")