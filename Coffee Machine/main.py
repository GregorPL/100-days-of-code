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

while True:
    choice = input("What would you like? (espresso/latte/cappuccino) ")

    if choice == "off":
        print("Turning off...")
        break
    
    if choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")

    if choice.lower() in ["espresso", "latte", "cappuccino"]:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.1
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01

        user_coins = sum([quarters, dimes, nickels, pennies])

        if user_coins < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")

    else:
        print("Sorry, we don't have this coffee in the menu :(")
