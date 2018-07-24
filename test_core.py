from core import *


def test_create_item_dictionary():
    item_dictionary = create_item_dictionary([
        'laptop, 16, 12.00, 40.00\n', 'flat-screen, 1, 50.00, 100.00\n',
        'table, 4, 10.00, 20.00\n'
    ])
    assert item_dictionary == {
        'laptop': {
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }


def test_remove_from_stock():
    inventory = {
        'laptop': {
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }
    assert remove_from_stock(inventory, 'laptop') == {
        'laptop': {
            'In-stock': 15,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }


def test_add_to_stock():
    inventory = {
        'laptop': {
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }
    assert add_to_stock(inventory, 'flat-screen') == {
        'laptop': {
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'In-stock': 2,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }


def test_create_file_string():
    inventory = {
        'laptop': {
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }
    assert create_file_string(
        inventory
    ) == 'item, in-stock, rent, replacement\nlaptop, 16, 12.0, 40.0\nflat-screen, 1, 50.0, 100.0\ntable, 4, 10.0, 20.0'
