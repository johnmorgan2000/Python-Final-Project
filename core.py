def create_item_list(inventory_info):
    item_list = []
    for info in inventory_info:
        product = info.split('\n')
        item_list.append(product)
    return item_list


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
