def open_inventory(filename):
    with open(filename) as file:
        file.readline()
        file_info = file.readlines()
    return file_info
