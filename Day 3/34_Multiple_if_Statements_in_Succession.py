print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))
ticket_price = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        ticket_price += 5
        print(f"Child tickets are € {ticket_price},-")
    elif age < 18:
        ticket_price += 7
        print(f"Youth tickets are € {ticket_price},-")
    elif age >= 65:
        ticket_price += 7
        print(f"Senior tickets are € {ticket_price},-")
    elif age >= 45 and age <= 55:
            print("Midlife crisis tickets are free!")
    else:
        ticket_price += 12
        print(f"Adult tickets are € {ticket_price},-")
    add_photo = input("Would you like a photo taken? Y or N: ")
    if add_photo == "Y" or add_photo == "y":
        ticket_price += 3
        print(f"With the photo included, your total bill is € {ticket_price},-")
    else:
        print(f"Without the photo, that'll be € {ticket_price},-")

else:
    print("I'm sorry, you're too short to ride this rollercoaster.")