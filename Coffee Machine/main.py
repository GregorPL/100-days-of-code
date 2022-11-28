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

profit = 0
machine_on = True

def chceck_resources(ordered_drink):
    for ingredient in ordered_drink:
        if ordered_drink[ingredient] > resources[ingredient]:
            print(f"Sorry there is not {ingredient} enough.")
            return False
        else:
            return True

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25 # $0.25
    total += int(input("how many dimes?: ")) * 0.1 # $0.1
    total += int(input("how many nickles?: ")) * 0.05 # $0.05
    total += int(input("how many pennies?: ")) * 0.01 # $0.01
    return total

def is_transaction_ok(user_money, drink_cost):
    if user_money >= drink_cost:
        change = round(user_money - drink_cost, 2)
        global profit 
        profit += drink_cost
        print(f"Here is {change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} :)")

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice in ["espresso", "latte", "cappuccino"]:
        menu_choice = MENU[choice]
        if chceck_resources(menu_choice['ingredients']):
            total = process_coins()

            if is_transaction_ok(total, menu_choice['cost']):
                make_coffee(choice, menu_choice['ingredients'])

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    
    elif choice == "off":
        machine_on = False