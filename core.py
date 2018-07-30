import datetime

date = datetime.datetime.now()


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
    if inventory[item_name]['In-stock'] > 0:
        inventory[item_name]['In-stock'] -= 1
        return inventory
    else:
        inventory[item_name]['In-stock'] == 0
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
    file_string = 'id_num, name, in-stock, rent, replacement'
    for key in inventory:
        file_string += f"\n{key},{inventory[key]['Name']}, {inventory[key]['In-stock']}, {inventory[key]['Rent']}, {inventory[key]['Value']}"
    return file_string


def create_history_string(date, inventory, response, action):
    history_string = f"{date}: {inventory[response]['Name']}, {action},  In-stock: {inventory[response]['In-stock']}\n"
    return history_string


def renting_total(inventory, cart):
    total = 0
    for item_name in cart:
        total += inventory[item_name]['Rent']
    return total


def replacement_fee(inventory, item_name):
    fee = inventory[item_name]['Value'] * .10
    return fee


def total_replacement_fee(inventory, cart):
    total = 0
    for item_name in cart:
        total += replacement_fee(inventory, item_name)
    return total


def create_revenue_dictionary(file_info):
    revenue_dictionary = {}
    for number in file_info:
        items = number.split(',')
        key = items[0]
        value = float(items[1].strip())
        revenue_dictionary[key] = value
    return revenue_dictionary


def create_revenue_string(revenue):
    revenue_string = "Revenue,{:.2f}".format(round(revenue['Revenue'], 2))
    return revenue_string


def add_revenue(revenue, total):
    revenue['Revenue'] += total
    return revenue


def subtract_revenue(revenue, deposit):
    revenue['Revenue'] -= deposit
    return revenue
