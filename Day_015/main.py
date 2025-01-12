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

    elif choice == "off":
        machine_working = False
        print("Bye !")

