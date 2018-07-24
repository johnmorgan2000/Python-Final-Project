def open_inventory(filename):
    with open(filename) as file:
        file.readline()
        file_info = file.readlines()
    return file_info


def write_file(filename, file_string):
    with open(filename, 'w') as file:
        file.write(file_string)
