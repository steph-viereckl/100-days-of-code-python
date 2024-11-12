from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#################################
# Start of program
#################################

# Create instance of Coffee Machine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on is True:

    user_input = input(f'Welcome! What would you like to drink? Type {menu.get_items()}: ').lower()

    # If user types "report" then print out report of current inventory
    if user_input == 'report':

        coffee_maker.report()
        money_machine.report()

    # If user types "off" then turn off machine
    elif user_input == 'off':

        machine_on = False
        print('Turning off for maintenance. Goodbye.')

    # Otherwise process their input
    else:

        # Find drink order in the menu
        drink_order = menu.find_drink(user_input)

        # If a valid drink order, proceed
        if drink_order is not None:

            # Check if there are sufficient ingredients
            if coffee_maker.is_resource_sufficient(drink_order) is True:

                # Collect Money
                if money_machine.make_payment(drink_order.cost) is True:

                    # Make Coffee!
                    coffee_maker.make_coffee(drink_order)


