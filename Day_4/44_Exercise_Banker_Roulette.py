# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# use randint to randomy select an index between 0 and the number of names in the list -1 (-1 because in a list with 3 items there's no indexnr 3)
import random

de_sjaak = names[random.randint(0,(len(names)-1))]

print(f"{de_sjaak} is going to pay the bill today!")

# random.choice(names) would've been an option :)