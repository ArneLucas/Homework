MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report():
    """Prints formatted report"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(
        f"Water: {water} ml\nMilk: {milk} ml\nCoffee: {coffee} gr\nMoney: € {money}")


def refill_machine(resources):
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("Thanks for refilling.")


def check_resources(MENU, coffee_choice):
    """Checks if enough resources for coffee of choice"""
    water = MENU[coffee_choice]["ingredients"]["water"]
    milk = MENU[coffee_choice]["ingredients"]["milk"]
    coffee = MENU[coffee_choice]["ingredients"]["coffee"]
    if resources["water"] - water < 0:
        print("Please refill water")
    elif resources["milk"] - milk < 0:
        print("Please refill milk")
    elif resources["coffee"] - coffee < 0:
        print("Please refill coffee")
    else:
        process_payment(MENU)


def process_payment(MENU):
    """Takes cost of coffee of choice, counts coins, and activates coffee making process"""
    total_paid = 0
    cost = float(MENU[coffee_choice]["cost"])
    while total_paid < cost:
        print(f"That'll be € {cost}. Please insert coins.")
        total_paid += 0.25 * int(input("How many quarters? "))
        total_paid += 0.10 * int(input("How many dimes? "))
        total_paid += 0.05 * int(input("How many nickles? "))
        total_paid += 0.01 * int(input("How many pennies? "))
        if cost == total_paid:
            print("Thank you")
            make_coffee(coffee_choice, resources, MENU)
        elif cost > total_paid:
            print(
                f"Sorry, that's not enoug money. € {total_paid} will be refunded")
        else:
            refund = total_paid - cost
            print(f"Here's € {refund} in change.")
            make_coffee(MENU, coffee_choice)


def make_coffee(MENU, coffee_choice):
    """Makes coffee of choice, and deducts resources"""
    resources["money"] += MENU[coffee_choice]["cost"]
    resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
    resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
    print(f"Enjoy your {coffee_choice} ☕. Next costumer please.")


machine_on = True
while machine_on:
    coffee_choice = input(
        "What would you like? (espresso/latte/cappuccino):\n").lower()
    if coffee_choice == "off":
        machine_on = False
    elif coffee_choice == "report":
        print_report()
    elif coffee_choice == "refill":
        refill_machine(resources)
    else:
        check_resources(MENU, coffee_choice)
