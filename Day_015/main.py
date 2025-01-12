from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def print_report():
    for key, amount in resources.items():
        if key in ['water', 'milk']:
            print(f"{key}: {amount}ml")
        elif key == "coffee":
            print(f"{key}: {amount}g")
        elif key == "money":
            print(f"{key}: ${amount:.2f}")

def check_resources_sufficient(drink):
    choice_ingredients = MENU[drink]["ingredients"]
    matching_ingredients = choice_ingredients & resources.keys()
    for items in matching_ingredients:
        if resources[items] < choice_ingredients[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True

def calculate_value_inserted():
    print("Please insert coins:")
    quarter = int(input("How may quarters?"))
    dimes = int(input("How may dimes?"))
    nickles = int(input("How may nickles?"))
    pennies = int(input("How may pennies?"))

    value_inserted = quarter * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    return value_inserted

machine_working = True

while machine_working:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
       print_report()
    elif choice in MENU:
        if not check_resources_sufficient(choice):
            print("Shutting down the coffee machine due to insufficient resources.")
            machine_working = False
            continue

        value = calculate_value_inserted()
        if value < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            resources["money"] += MENU[choice]["cost"]
            change = value - MENU[choice]["cost"]
            print(f"Here is ${change:.2f} dollars in change")
            common_ingredients = MENU[choice]["ingredients"] & resources.keys()
            for ingredients in common_ingredients:
                resources[ingredients] -= MENU[choice]["ingredients"][ingredients]
            print(f"Here is your {choice}. Enjoy!")
    elif choice == "off":
        machine_working = False
        print("Shutting down coffee machine...")

