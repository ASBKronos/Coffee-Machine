menu = {
    "espresso":
        {"ingredients": {"water": 50, "coffee": 18,}, "cost": 1.5,},
    "latte":
        {"ingredients": {"water": 200,"milk": 150,"coffee": 24,},"cost": 2.5,},
    "cappuccino":
        {"ingredients": {"water": 250,"milk": 100,"coffee": 24,},"cost": 3.0,}}

resources = {"water": 300,"milk": 200,"coffee": 100,}


machine_is_on = True
profit = 0 #Machine has an empty money box in the beginning


def check_resources(drinks):
    '''Returns True if order can be made or False if ingredients are insufficient '''
    for i in drinks:
        if drinks[i] >= resources[i]:
            print(f"Sorry! There is not enough {i}")
            return False
    else:
        return True


def collect_coins():
    '''Returns the total calculated from coins inserted'''
    total = 0
    total = int(input("How Many Quarters?")) * 0.25
    total += int(input("How Many Dimes?")) * 0.10
    total += int(input("How Many Nickles?")) * 0.05
    total += int(input("How Many Pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, user_choice):
    '''Returns True if money is accepted or False if payment is insufficient'''
    global profit
    if money_received < user_choice["cost"]:
        print("Sorry. That's not enough money. Money Refunded!")
        return False
    else:
        change = round(money_received - user_choice["cost"],2)
        print(f"Here is ${change} in change.")
        profit += money_received
        return True


def make_coffee(drink_ingredients,drink_name):
    '''Deduct the required ingredients from the resources available'''
    for i in drink_ingredients:
        resources[i] -= drink_ingredients[i]
    print(f"Here is your {drink_name} ☕︎☕︎☕︎ ")
    return True


while machine_is_on:
    choice = input("What would you like to order? (Espresso/Latte/Cappuccino): ").lower()

    if choice == 'off':
        machine_is_on = False
    elif choice == 'report':
        print(f"Milk: {resources['water']}ml")
        print(f"Water: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu[choice]
        if check_resources(drink['ingredients']):       #If there are enough ingredients for the choice of user drink, then
            money_inserted = collect_coins()
            if is_transaction_successful(money_inserted, drink):
                make_coffee(drink['ingredients'],choice)


