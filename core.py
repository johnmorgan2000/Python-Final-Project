def create_item_dictionary(item_list):
    item_dictionary = {}
    for product in item_list:
        items = product.split(',')
        key = items[0]
        value = {
            'In-stock': int(items[1]),
            'Rent': float(items[2]),
            'Value': float(items[3])
        }
        item_dictionary[key] = value
    return item_dictionary


def remove_from_stock(inventory, item_name):
    inventory[item_name]['In-stock'] -= 1
    return inventory


def add_to_stock(inventory, item_name):
    inventory[item_name]['In-stock'] += 1
    return inventory


def create_file_string(inventory):
    file_string = 'item, in-stock, rent, replacement'
    for key in inventory:
        file_string += f"\n{key}, {inventory[key]['In-stock']}, {inventory[key]['Rent']}, {inventory[key]['Value']}"
    return file_string
