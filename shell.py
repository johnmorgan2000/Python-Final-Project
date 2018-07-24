import disk
import core


def greeting():
    print('Welcome to Base Camp\'s Rentals')


def user_or_employee():
    while True:
        response = input('[U]ser or [E]ployee? >>> ').upper().strip()
        if response == 'U':
            return user_action()
        #elif response == 'E':
        else:
            print('Not a valid entry.')


def user_action():
    while True:
        response = input('Are you [1]renting or [2]returning? >>>')
        if response == '1':
            return renting()
        elif response == '2':
            return returning()


def reting():

    response = input('What would you like to rent today?')


def main():
    inventory_info = disk.open_inventory('inventory.txt')
    print(inventory_info)
    print(core.create_item_list(inventory_info))
    greeting()
    user_or_employee()


if __name__ == '__main__':
    main()
