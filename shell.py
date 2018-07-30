import disk
import core
import datetime


def greeting():
    print()
    print('Welcome to Base Camp\'s Rentals')
    while True:
        response = input("[1] Continue\n[2] Close\n>>> ").strip()
        print()
        if response == '1':
            return None
        elif response == '2':
            print('Ok, see you later.')
            exit()
        else:
            print('Please use 1 or 2 to answer')


def print_inventory(inventory):
    print('\n-x-x-x-x-INVENTORY-x-x-x-x-')
    for key in inventory:
        print(
            "{} (ID:{})\n--In-stock: {}  Renting Price: {:0.2f}  Value: {:0.2f}".
            format(inventory[key]['Name'], key, inventory[key]['In-stock'],
                   inventory[key]['Rent'], inventory[key]['Value']))
    print('-x-x-x-x-x-x-x-x-x-x-x-x-x-\n')


def print_stock(inventory):
    for key in inventory:
        print("{} ({}) -- In stock: {}".format(inventory[key]['Name'], key,
                                               inventory[key]['In-stock']))


def print_return_item_list(inventory):
    for key in inventory:
        print("ID: {}  Item: {}".format(key, inventory[key]['Name']))


def user_or_employee(date, inventory, cart, revenue):
    while True:
        response = input('[U]ser or [E]mployee? >>> ').upper().strip()
        if response == 'U':
            return user_action(date, inventory, cart, revenue)
        elif response == 'E':
            return employee_action(inventory, revenue)
        else:
            print('Not a valid entry.')


def user_action(date, inventory, cart, revenue):
    while True:
        response = input('Are you [1]renting or [2]returning? >>> ')
        if response == '1':
            return renting(date, inventory, cart)
        elif response == '2':
            return returning(date, inventory, revenue)


def employee_action(inventory, revenue):
    while True:
        response = input(
            "\nEnter an action.\n[1] Stock\n[2] Transaction History\n[3] Total Revenue\n[4] Quit\n>>> "
        )
        print()
        if response == '1':
            print_stock(inventory)
        elif response == '2':
            print(disk.history_contents('history.txt'))
        elif response == '3':
            print("Total Revenue: ${:.2f}".format(revenue['Revenue']))
        elif response == '4':
            main()
        else:
            print('Invalid Number')


def renting(date, inventory, cart):
    print_inventory(inventory)
    while True:
        response = input(
            'What would you like to rent today? Use a valid ID number.\n>>> '
        ).lower().strip()
        if response in inventory:
            if core.in_stock(inventory, response) == True:
                cart.append(response)
                core.remove_from_stock(inventory, response)
                disk.update_history(date, 'history.txt', inventory, response,
                                    'Rented')
                print(
                    "Your item ({}) will cost you {:0.2f} to rent for the week.".
                    format(inventory[response]['Name'],
                           inventory[response]['Rent']))
                return add_more_to_cart(date, inventory, cart)
            elif core.in_stock(inventory, response) == False:
                print('Item is currently out of stock. Sorry')
        else:
            print(
                'Not a valid option. Please check your spelling and try again.'
            )


def returning(date, inventory, revenue):
    while True:
        print_return_item_list(inventory)
        response = input(
            'What are you returning?\nEnter in an ID number or type in [Q] to quit>>> '
        ).lower().strip()
        if response in inventory:
            core.add_to_stock(inventory, response)
            deposit = core.replacement_fee(inventory, response)
            disk.update_inventory(inventory, 'inventory.txt')
            disk.update_history(date, 'history.txt', inventory, response,
                                'Returned')
            print(
                f'\nThank you for returning this item.\nHere is your deposit back ${deposit}\n'
            )
            core.subtract_revenue(revenue, deposit)
            disk.update_revenue(revenue, 'revenue.txt')
        elif response == 'q':
            print('Goodbye')
            main()
        else:
            ('This is not a returnable item here, sorry?')


def add_more_to_cart(date, inventory, cart):
    while True:
        more = input(
            'Would you like anything else, [Y] or [N]?\n>>> ').upper().strip()
        if more == 'Y':
            return renting(date, inventory, cart)
        elif more == 'N':
            print('OK, lets checkout')
            disk.update_inventory(inventory, 'inventory.txt')
            return inventory, cart
        else:
            print('Not a valid input')


def create_receipt(inventory, cart, revenue):
    print('\n--Your Receipt--\nItems:')
    for item_name in cart:
        print("{}  Rent: ${:0.2f}  10% Replacement Fee: {:0.2f}".format(
            inventory[item_name]['Name'], round(inventory[item_name]['Rent'],
                                                2),
            round(core.replacement_fee(inventory, item_name), 2)))
    total = receipt_total(inventory, cart, revenue)
    disk.update_revenue(revenue, 'revenue.txt')
    print('Total: ${:0.2f}'.format(round(total, 2)))
    print('Thank you, goodbye\n')


def receipt_total(inventory, cart, revenue):
    rent = core.renting_total(inventory, cart)
    fee = core.total_replacement_fee(inventory, cart)
    total = (rent * 1.07) + fee
    core.add_revenue(revenue, total)
    return total


def main():
    date = datetime.datetime.now()
    cart = []
    inventory_info = disk.open_inventory('inventory.txt')
    revenue_info = disk.open_revenue('revenue.txt')
    inventory = core.create_item_dictionary(inventory_info)
    revenue = core.create_revenue_dictionary(revenue_info)

    greeting()
    inventory, cart = user_or_employee(date, inventory, cart, revenue)
    create_receipt(inventory, cart, revenue)

    main()


if __name__ == '__main__':
    main()
