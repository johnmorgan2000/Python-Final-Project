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
