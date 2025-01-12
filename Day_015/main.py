from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources_sufficient(drink):
    choice_ingredients = MENU[drink]["ingredients"]
    common_ingredients = choice_ingredients & resources.keys()
    for ingredients in common_ingredients:
        if resources[ingredients] < choice_ingredients[ingredients]:
            print(f"Sorry there is not enough {ingredients}")
            return False
    return True

machine_working = True

while machine_working:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        # Print the report
        for key, value in resources.items():
            if key in ['water', 'milk']:
                print(f"{key}: {value}ml")
            elif key == "coffee":
                print(f"{key}: {value}g")
            elif key == "money":
                print(f"{key}: ${value:.2f}")
    elif choice in MENU:
        check_resources_sufficient(choice)
        print("Please insert coins:")
        quarter = int(input("How may quarters?"))
        dimes = int(input("How may dimes?"))
        nickles = int(input("How may nickles?"))
        pennies = int(input("How may pennies?"))

        value_inserted = quarter*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

        if value_inserted < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            resources["money"] += MENU[choice]["cost"]
            change = value_inserted-MENU[choice]["cost"]
            print(f"Here is ${change:.2f} dollars in change")
            common_ingredients = MENU[choice]["ingredients"] & resources.keys()
            for ingredients in common_ingredients:
                resources[ingredients] -= MENU[choice]["ingredients"][ingredients]
            print(f"Here is your {choice}. Enjoy!”")
    elif choice == "off":
        machine_working = False
        print("Shutting down coffee machine...")

