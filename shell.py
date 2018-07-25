import disk
import core


def greeting():
    print('Welcome to Base Camp\'s Rentals')


def print_inventory(inventory):
    print('\n-x-x-x-x-INVENTORY-x-x-x-x-')
    for key in inventory:
        print(
            f"Item:{inventory[key]['Name']}\n-In-stock: {inventory[key]['In-stock']}  Renting Price: {inventory[key]['Rent']}  Value: {inventory[key]['Value']}"
        )
    print('-x-x-x-x-x-x-x-x-x-x-x-x-x-\n')


def user_or_employee(inventory, cart):
    while True:
        response = input('[U]ser or [E]mployee? >>> ').upper().strip()
        if response == 'U':
            return user_action(inventory, cart)
        elif response == 'E':
            return employee_action()
        else:
            print('Not a valid entry.')


def user_action(inventory, cart):
    while True:
        response = input('Are you [1]renting or [2]returning? >>>')
        if response == '1':
            return renting(inventory, cart)
        elif response == '2':
            return returning(inventory)


#def employee_action():
#    print("[1] Stock\n[2] Transaction History\n [3] Total Revenue\n")
#    while True:
#        if response == '1':
#            print_inventory()


def renting(inventory, cart):
    print_inventory(inventory)
    while True:
        response = input(
            'What would you like to rent today?\n>>> ').lower().strip()
        if response in inventory:
            if core.in_stock(inventory, response) == True:
                cart.append(response)
                core.remove_from_stock(inventory, response)
                disk.update_history('history.txt', inventory, response,
                                    'Renting')
                return add_more_to_cart(inventory, cart)
            elif core.in_stock(inventory, response) == False:
                print('Item is currently out of stock. Sorry')
        else:
            print(
                'Not a valid option. Please check your spelling and try again.'
            )


def returning(inventory):
    while True:
        response = input(
            'What are you returning?\nEnter in an item or type in [Q] to quit>>> '
        ).lower().strip()
        if response in inventory:
            core.add_to_stock(inventory, response)
            deposit = core.replacement_fee(inventory, response)
            disk.update_inventory(inventory, 'inventory.txt')
            disk.update_history('history.txt', inventory, response, 'Returned')
            print(
                f'\nThank you for returning this item.\nHere is your deposit back ${deposit}\n'
            )
        elif response == 'q':
            print('Goodbye')
            exit()
        else:
            ('This is not a returnable item here, sorry?')


def add_more_to_cart(inventory, cart):
    while True:
        more = input('Would you like anything else, [Y] or [N]?\n>>> ').upper()
        if more == 'Y':
            renting(inventory, cart)
        elif more == 'N':
            print('OK, lets checkout')
            disk.update_inventory(inventory, 'inventory.txt')
            return inventory, cart
        else:
            print('Not a valid input')
        return inventory, cart


def create_receipt(inventory, cart):
    print('\n--Your Receipt--')
    for item_name in cart:
        print(
            f"Items: {inventory[item_name]['Name']}  Rent: ${inventory[item_name]['Rent']}  10% Replacement Fee: {core.replacement_fee(inventory,item_name)}"
        )
    rent = core.renting_total(inventory, cart)
    fee = core.total_replacement_fee(inventory, cart)
    total = rent + fee
    print(f'Total: ${total}')


def main():
    cart = []
    inventory_info = disk.open_inventory('inventory.txt')
    inventory = core.create_item_dictionary(inventory_info)
    greeting()
    inventory, cart = user_or_employee(inventory, cart)
    create_receipt(inventory, cart)


if __name__ == '__main__':
    main()
