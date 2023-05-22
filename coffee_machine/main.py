from menu import MENU, resources
profit = 0
machine_on = True


def money():
    """Returns total money received from coins inserted by the user."""
    money_received = 0
    quarter = int(input("How many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickel = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    money_received += (quarter * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (pennies * 0.01)
    return money_received


def resource_manager(coffee_name):
    """ Takes name of the coffee and update the resource dictionary."""
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    if coffee_name == 'espresso':
        water -= MENU[coffee_name]['ingredients']['water']
        coffee -= MENU[coffee_name]['ingredients']['coffee']
    elif coffee_name == 'latte' or coffee_name == 'cappuccino':
        water -= MENU[coffee_name]['ingredients']['water']
        coffee -= MENU[coffee_name]['ingredients']['coffee']
        milk -= MENU[coffee_name]['ingredients']['milk']
    resources['water'] = water
    resources['coffee'] = coffee
    resources['milk'] = milk
    return resources


def working(choice_of_user):
    global profit
    if choice_of_user == 'espresso' or choice_of_user == 'latte' or choice_of_user == 'cappuccino':
        cost_of_coffee = MENU[choice_of_user]['cost']
        if resources['water'] >= MENU[choice_of_user]['ingredients']['water']:
            print("Please insert coin.")
            money_received = money()
            if money_received >= cost_of_coffee:
                change = round(money_received - cost_of_coffee, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice_of_user} ☕. Enjoy!")
                profit += cost_of_coffee
                resource_manager(choice_of_user)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Out of ingredients")
    elif choice_of_user == 'report':
        print(f" water: {resources['water']}ml,\n milk: {resources['milk']}ml,\n coffee:"
              f" {resources['coffee']}gm,\n money: ${profit}")


while machine_on:
    choice = input("What would you like? (espresso = $1.5/latte = $2.5/cappuccino = $3.0): ").lower()
    if choice == 'off':
        machine_on = False

    elif choice == 'espresso' or 'latte' or 'cappuccino':
        working(choice)

