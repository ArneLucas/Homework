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

# penny     € 0,01
# nickel    € 0,05
# dime      € 0,10
# quarter   € 0,25


def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(
        f"Water: {water} ml\nMilk: {milk} ml\nCoffee: {coffee} gr\nMoney: € {money}")


def check_resources(MENU, coffee_choice):
    water = MENU[coffee_choice]["ingredients"]["water"]
    milk = MENU[coffee_choice]["ingredients"]["milk"]
    coffee = MENU[coffee_choice]["ingredients"]["coffee"]
    if resources["water"] - water < 0:
        return "Please refill water"
    elif resources["milk"] - milk < 0:
        return "Please refill milk"
    elif resources["coffee"] - coffee < 0:
        return "Please refill coffee"
    else:
        process_payment(MENU)


def make_coffee(MENU, coffee_choice):
    resources["money"] += MENU[coffee_choice]["cost"]
    resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
    resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
    print(f"Enjoy your {coffee_choice} ☕. Next costumer please.")


def process_payment(MENU):
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
        else:
            refund = total_paid - cost
            print(f"Here's € {refund} in change.")
            make_coffee(MENU, coffee_choice)


# TODO: Prompt user by asking “​What would you like? (espresso/latte/cappuccino)
machine_on = True
while machine_on:
    coffee_choice = input(
        "What would you like? (espresso/latte/cappuccino):\n").lower()
    # TODO: Turn off the Coffee Machine by entering “​off​” to the prompt
    if coffee_choice == "off":
        machine_on = False
    # TODO: Print report.
    elif coffee_choice == "report":
        print_report()
    else:
        check_resources(MENU, coffee_choice)


# TODO: Check resources sufficient?
# TODO: Process coins.
# TODO: Check transaction successful?
