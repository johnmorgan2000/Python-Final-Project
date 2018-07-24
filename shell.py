import disk
import core


def greeting():
    print('Welcome to Base Camp\'s Rentals')


def print_inventory(inventory):
    for key in inventory:
        print(
            f"Item:{inventory[key]['Name']}\n-In-stock: {inventory[key]['In-stock']}  Renting Price: {inventory[key]['Rent']}  Value: {inventory[key]['Value']}"
        )


def user_or_employee(inventory, cart):
    while True:
        response = input('[U]ser or [E]mployee? >>> ').upper().strip()
        if response == 'U':
            return user_action(inventory, cart)
        #elif response == 'E':
        else:
            print('Not a valid entry.')


def user_action(inventory, cart):
    while True:
        response = input('Are you [1]renting or [2]returning? >>>')
        if response == '1':
            return renting(inventory, cart)
        elif response == '2':
            return returning()


def renting(inventory, cart):
    print_inventory(inventory)
    while True:
        response = input(
            'What would you like to rent today?\n>>> ').lower().strip()
        if response in inventory:
            cart.append(f"{inventory[response]['Name']}")
            core.remove_from_stock(inventory, response)
            return add_more_to_cart(inventory, cart)
        else:
            print(
                'Not a valid option. Please check your spelling and try again.'
            )


def add_more_to_cart(inventory, cart):
    while True:
        more = input('Would you like anything else, [Y] or [N]?\n>>> ').upper()
        if more == 'Y':
            renting(inventory, cart)
        elif more == 'N':
            print('OK, lets checkout')
            return cart
        else:
            print('Not a valid input')


def main():
    cart = []
    inventory_info = disk.open_inventory('inventory.txt')
    inventory = core.create_item_dictionary(inventory_info)
    greeting()
    user_or_employee(inventory, cart)
    print(cart)
    print(inventory)


if __name__ == '__main__':
    main()
