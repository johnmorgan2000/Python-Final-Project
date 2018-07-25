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
        file.readline()
        file.readlines()


def write_history(filename, history_string):
    with open(filename, 'a') as file:
        file.write(history_string)


def update_inventory(inventory, filename):
    file_string = core.create_file_string(inventory)
    write_file(filename, file_string)


def update_history(filename, inventory, response, action):
    history_string = core.create_history_string(inventory, response, action)
    write_history(filename, history_string)


def print_history(filename):
    with open(filename) as file:
        print(file)
