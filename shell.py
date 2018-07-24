import disk
import core


def greeting():
    print('Welcome to Base Camp\'s Rentals')


def print_inventory(inventory):
    for key in inventory:
        print(
            f"Item:{key}\n-In-stock: {inventory[key]['In-stock']}  Renting Price: {inventory[key]['Rent']}  Value: {inventory[key]['Value']}"
        )


def user_or_employee(inventory):
    while True:
        response = input('[U]ser or [E]ployee? >>> ').upper().strip()
        if response == 'U':
            return user_action(inventory)
        #elif response == 'E':
        else:
            print('Not a valid entry.')


def user_action(inventory):
    while True:
        response = input('Are you [1]renting or [2]returning? >>>')
        if response == '1':
            return renting(inventory)
        elif response == '2':
            return returning()


def renting(inventory):
    print_inventory(inventory)
    response = input('What would you like to rent today?')


def main():
    inventory_info = disk.open_inventory('inventory.txt')
    inventory = core.create_item_dictionary(inventory_info)
    greeting()
    user_or_employee(inventory)


if __name__ == '__main__':
    main()
