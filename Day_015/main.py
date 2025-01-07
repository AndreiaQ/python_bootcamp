from menu import MENU

choice = input("What would you like? (espresso/latte/cappuccino):").lower()

while choice != "off":
    drink = MENU
    resources = {
        "water": 30,
        "milk": 200,
        "coffee": 10,
        "money": 0
    }
    if choice == "report":
        for key, value in resources.items():
            if key == 'water' or key == 'milk':
                print(f"{key}: {value}ml")
            elif key == "coffee":
                print(f"{key}: {value}g")
            elif key == "money":
                print(f"{key}: ${value}")
        break
    if choice == "espresso":
        espresso_ingredients = drink["espresso"]["ingredients"]
        common_ingredients = resources.keys() & espresso_ingredients.keys()
        for ingredient in common_ingredients:
            if resources[ingredient] < espresso_ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
        break

    break


