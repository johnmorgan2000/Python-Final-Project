def create_item_dictionary(item_list):
    item_dictionary = {}
    for product in item_list:
        items = product.split(',')
        key = items[0]
        value = {
            'Name': (items[1]),
            'In-stock': int(items[2]),
            'Rent': float(items[3]),
            'Value': float(items[4])
        }
        item_dictionary[key] = value
    return item_dictionary


def remove_from_stock(inventory, item_name):
    inventory[item_name]['In-stock'] -= 1
    return inventory


def add_to_stock(inventory, item_name):
    inventory[item_name]['In-stock'] += 1
    return inventory


def in_stock(inventory, item_name):
    if inventory[item_name]['In-stock'] <= 0:
        inventory[item_name]['In-stock'] = 0
        return False
    elif inventory[item_name]['In-stock'] > 0:
        return True


def create_file_string(inventory):
    file_string = 'item, name, in-stock, rent, replacement'
    for key in inventory:
        file_string += f"\n{key},{inventory[key]['Name']}, {inventory[key]['In-stock']}, {inventory[key]['Rent']}, {inventory[key]['Value']}"
    return file_string


def create_history_string(inventory, action):
    history_string = 'item, action, in-stock'
    for key in inventory:
        history_string += f"\nItem: {inventory[key]['Name']},  Action: {action},  In-stock: {inventory[key]['In-stock']}"
    return history_string


def renting_total(inventory, cart):
    total = 0
    for item_name in cart:
        total += inventory[item_name]['Rent']
    return total


def replacement_fee(inventory, item_name):
    fee = inventory[item_name]['Value'] * .10
    return fee
