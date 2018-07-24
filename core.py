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
