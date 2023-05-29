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
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}
money = 0

from art import coffee_logo

def update_resources(item_bought):
    resources["water"] -= MENU[item_bought]["ingredients"]["water"]
    resources["coffee"] -= MENU[item_bought]["ingredients"]["coffee"]
    if item_bought != "espresso":
        resources["milk"] -= MENU[item_bought]["ingredients"]["milk"]
    global money
    money += MENU[item_bought]["cost"]


def process_coins():
    # TODO: 3. Process coins
    paid_amount = 0
    print("Please insert coins.")
    paid_amount += int(input("How many quarters? ")) * 0.25
    paid_amount += int(input("How many dimes? ")) * 0.1
    paid_amount += int(input("How many nickels? ")) * 0.05
    paid_amount += int(input("How many pennies? ")) * 0.01
    return paid_amount

# TODO: 2. Check resources  sufficient?
def check_resource_availability(user_choice):
    water_available = (resources["water"] >= MENU[user_choice]["ingredients"]["water"])
    coffee_available = (resources["coffee"] >= MENU[user_choice]["ingredients"]["coffee"])
    if user_choice == "espresso":
        if water_available and coffee_available:
            return True
        else:
            return False
    elif user_choice == "latte" or user_choice == "cappuccino":
        milk_available = (resources["milk"] >= MENU[user_choice]["ingredients"]["milk"])
        if water_available and coffee_available and milk_available:
            return True
        else:
            return False
    else:
        print("Invalid choice!")


print(coffee_logo)
machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 1. Print report
    if user_choice == "off":
        print("Turning off")
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        resources_available = check_resource_availability(user_choice)
        if not resources_available:
            print(f"{user_choice} is not available.")
        else:
            paid_amount = process_coins()
            # TODO: 4. Check transaction successful?
            price_of_coffee = MENU[user_choice]["cost"]
            diff = paid_amount - price_of_coffee
            if diff < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if diff > 0:
                    print(f"Here is your ${round(diff, 2)} in change.")
                # TODO: 5. Make coffee.
                print(f"Here is your {user_choice} ☕. Enjoy!")
                update_resources(user_choice)






