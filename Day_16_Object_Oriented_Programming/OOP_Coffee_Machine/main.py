from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
# menu_item = MenuItem()

machine_on = True
while machine_on:
    options = menu.get_items()
    coffee_choice = input(
        f"What would you like? {options}:\n").lower()
    if coffee_choice == "off":
        machine_on = False
    elif coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
