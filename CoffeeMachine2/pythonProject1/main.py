MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

inventory = {
    'water': {'amount': 300, 'measurement': 'ml'},
    'milk': {'amount': 200, 'measurement': 'ml'},
    'coffee': {'amount': 100, 'measurement': 'g'},
    'money': {'amount': 0, 'measurement': '$'}
}

def print_report():
    """Print out the current inventory levels"""
    for ingredient in inventory:

        amount = inventory[ingredient]['amount']
        measurement = inventory[ingredient]['measurement']

        if ingredient != 'money':
            print(f'{ingredient}: {amount}{measurement}')
        else:
            print(f'{ingredient}: {measurement}{format(amount, '.2f')}')

def check_ingredient_levels(drink):
    """For the current drink, check to see if there are enough resources
    Return True if there are enough, otherwise return False
    """
    # Loop through all ingredients (i.e. water, milk, coffee)
    for ingredient in inventory:

        # Skip 'Money' since this is not an ingredient required to generate drink
        if ingredient in MENU[drink]['ingredients'].keys():

            # For the specified drink, find the required amount of the current ingredient
            required_ingredient = MENU[drink]['ingredients'][ingredient]

            # Find the current inventory for that ingredient
            current_inventory_amount = inventory[ingredient]['amount']

            # If the drink requires more ingredients than are in the supply, return false
            if required_ingredient > current_inventory_amount:
                print(f'There is not enough {ingredient}')
                return False

    # If there are enough ingredients, return true
    return True

def reduce_ingredients(drink):
    """Reduce the inventory for the drink the user ordered"""

    # Loop through all ingredients (i.e. water, milk)
    for ingredient in inventory:

        # Only reduce ingredients that the drink calls for
        if ingredient in MENU[drink]['ingredients'].keys():

            inventory[ingredient]['amount'] -= MENU[drink]['ingredients'][ingredient]
            print(f'.... Reduce {ingredient.title()} by: {MENU[drink]['ingredients'][ingredient]}')

def format_to_int(coins_entered):
    """Convert user entry to valid integer or throw exception"""
    if coins_entered.isdigit() is True:
        return int(coins_entered)
    else:
        raise Exception("Sorry, you did not enter a valid number. Please try again.")


def collect_money():
    """Prompt user to enter money and return the total amount entered"""
    print('Please insert coins: ')

    num_quarters = format_to_int(input('How many quarters?: '))
    num_dimes = format_to_int(input('How many dimes?: '))
    num_nickles = format_to_int(input('How many nickles?: '))
    num_pennies = format_to_int(input('How many pennies?: '))

    sum = 0
    sum += num_quarters * .25
    sum += num_dimes * .10
    sum += num_nickles * .05
    sum += num_pennies * .01

    print(f'Total amount entered: ${sum}')

    return sum

def verify_transaction(user_money, drink):
    """Check to see if the amount entered is sufficient to cover the cost of the drink"""

    cost_of_drink = MENU[drink]['cost']
    print(f'Drink costs {cost_of_drink}')

    if user_money == cost_of_drink:
        print(f'Success! Here is your {drink}')
        inventory['money']['amount'] += cost_of_drink
        return True

    elif user_money > cost_of_drink:
        change = user_money - cost_of_drink
        print(f'Success! Here is your {drink} and change of {change}')
        inventory['money']['amount'] += cost_of_drink
        return True

    else:
        print('Sorry that is not enough money. Money refunded.')
        return False


#################################
# Start of program
#################################

machine_on = True

while machine_on is True:

    user_input = input('Welcome! What would you like to drink? Type \'Espresso\', \'Latte\' or \'Cappuccino\': ').lower()

    # If the user's input is in the Menu, then proceed
    if user_input in MENU.keys():

        # Check to ensure there are enough resources in the machine
        if check_ingredient_levels(user_input) is True:

            ## Collect money from user
            money_entered = collect_money()
            ## Pass in money collected and drink order
            verify_transaction(money_entered, user_input)
            ## Reduce inventory numbers
            reduce_ingredients(user_input)

        # If there are not enough ingredients for drink, let user know
        else:
            print(f'Insufficient resources!')

    # If user types "report" then print out report of current inventory
    elif user_input == 'report':
        print_report()

    # If user types "off" then turn off machine
    elif user_input == 'off':
        machine_on = False
        print('Turning off for maintenance. Goodbye.')

    # For all other inputs, ask user to try again (start next loop)
    else:
        print('Invalid order. Please try again or enter \'off\' to turn off machine')




