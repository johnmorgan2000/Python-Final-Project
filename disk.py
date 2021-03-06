import core


def open_inventory(filename):
    with open(filename) as file:
        file.readline()
        file_info = file.readlines()
    return file_info


def write_file(filename, file_string):
    with open(filename, 'w') as file:
        file.write(file_string)


def open_history(filename):
    with open(filename) as file:
        file.readlines()


def write_history(filename, history_string):
    with open(filename, 'a') as file:
        file.write(history_string)


def update_inventory(inventory, filename):
    file_string = core.create_file_string(inventory)
    write_file(filename, file_string)


def update_history(date, filename, inventory, response, action):
    history_string = core.create_history_string(date, inventory, response,
                                                action)
    write_history(filename, history_string)


def history_contents(filename):
    with open(filename) as file:
        contents = file.read()
    return contents


def open_revenue(filename):
    with open(filename) as file:
        file_info = file.readlines()
    return file_info


def write_revenue(filename, revenue_string):
    with open(filename, 'w') as file:
        file.write(revenue_string)


def update_revenue(revenue, filename):
    revenue_string = core.create_revenue_string(revenue)
    write_revenue(filename, revenue_string)
