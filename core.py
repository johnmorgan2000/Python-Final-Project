def create_item_list(inventory_info):
    item_list = []
    for info in inventory_info:
        product = info.split('\n')
        item_list.append(product)
    return item_list
