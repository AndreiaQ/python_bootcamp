from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_on = False
        print("Shutting down coffee machine...")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            coffee_maker.is_resource_sufficient(drink)
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
        else:
            print("Sorry we dont have that drink :(")





