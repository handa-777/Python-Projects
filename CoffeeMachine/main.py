from data import MENU, resources
money = 0
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${money}")


def make_coffee(coffee):
    is_possible = True
    keys = MENU[coffee]['ingredients'].keys()
    for item in keys:
        if resources[item] < MENU[coffee]['ingredients'][item]:
            is_possible = False
            shortage = item
            break
    if is_possible:
        for item in keys:
            resources[item] -= MENU[coffee]['ingredients'][item]
        calc_change(coffee)
        print(f"Here is your {coffee} ☕️. Enjoy!")
    else:
        print(f"Sorry there is not enough {shortage}.")


def calc_change(coffee):
    print("Please insert coins.")
    quart = float(input("How many quarters? "))
    dime = float(input("How many dimes? "))
    nick = float(input("How many nickles? "))
    penn = float(input("How many pennies? "))
    total = quart * 0.25 + dime * 0.10 + nick * 0.05 + penn * 0.01
    price = MENU[coffee]['cost']
    change = round(total - price, 2)
    if total < price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        global money
        money += price
        print(f"Here is ${change} in change.")


is_off = False
while not is_off:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "report":
        print_report()
    elif coffee == "off":
        is_off = True
    else:
        make_coffee(coffee)