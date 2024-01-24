MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

money = {
    "balance": 0
}


def coffee_machine():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        return None

    elif user_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f'Money: ${money["balance"]}')
        coffee_machine()
    else:
        is_enough = True
        for ingredient in MENU[user_input]["ingredients"]:
            if resources[ingredient] < MENU[user_input]["ingredients"][ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                is_enough = False

        if is_enough is False:
            coffee_machine()

        print("Please insert coins.")

        quarters = int(input("How many quarters? "))

        dimes = int(input("How many dimes? "))

        nickles = int(input("How many nickles? "))

        pennies = int(input("How many pennies? "))

        monetary_value = float(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)

        if monetary_value < MENU[user_input]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            coffee_machine()
        else:
            money["balance"] += MENU[user_input]["cost"]
            monetary_value -= MENU[user_input]["cost"]

            if "water" in MENU[user_input]["ingredients"]:
                resources["water"] -= MENU[user_input]["ingredients"]["water"]
            if "milk" in MENU[user_input]["ingredients"]:
                resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
            if "coffee" in MENU[user_input]["ingredients"]:
                resources["coffee"] -= MENU[user_input]["ingredients"]["water"]

        if monetary_value > 0:
            print(f"Here is ${round(monetary_value, 2)} dollars in change.")

        print(f"Here is you {user_input}. Enjoy! ☕️ ")

        coffee_machine()


coffee_machine()
