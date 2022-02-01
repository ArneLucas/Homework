print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("That'll be € 5,- please")
    elif age <= 18:
        print("That'll be € 7,- please")
    elif age > 65:
        print("That'll be € 7,- please")
    else:
        print("That'll be € 12,- please")
else:
    print("I'm sorry, you're too small to ride this rollercoaster.")