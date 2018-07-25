from core import *


def test_create_item_dictionary():
    item_dictionary = create_item_dictionary([
        'laptop,Laptop, 16, 12.00, 40.00\n',
        'flat-screen,Flat-screen, 1, 50.00, 100.00\n',
        'table,Table, 4, 10.00, 20.00\n'
    ])
    assert item_dictionary == {
        'laptop': {
            'Name': 'Laptop',
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'Name': 'Flat-screen',
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'Name': 'Table',
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
            'Name': 'Laptop',
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'Name': 'Flat-screen',
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'Name': 'Table',
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }
    assert create_file_string(
        inventory
    ) == 'item, name, in-stock, rent, replacement\nlaptop,Laptop, 16, 12.0, 40.0\nflat-screen,Flat-screen, 1, 50.0, 100.0\ntable,Table, 4, 10.0, 20.0'


def test_create_history_string():
    inventory = {
        'laptop': {
            'Name': 'Laptop',
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'Name': 'Flat-screen',
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'Name': 'Table',
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }
    assert create_history_string(
        inventory, 'laptop',
        'Rented') == 'Item: Laptop,  Action: Rented,  In-stock: 16\n'


def test_in_stock():

    inventory = inventory = {
        'laptop': {
            'Name': 'Laptop',
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'Name': 'Flat-screen',
            'In-stock': 0,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'Name': 'Table',
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }

    assert in_stock(inventory, 'laptop') == True
    assert in_stock(inventory, 'flat-screen') == False


def test_renting_total():
    cart = ['laptop', 'table']
    inventory = {
        'laptop': {
            'Name': 'Laptop',
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'Name': 'Flat-screen',
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'Name': 'Table',
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }
    assert renting_total(inventory, cart) == 22.0


def test_replacement_fee():
    inventory = {
        'laptop': {
            'Name': 'Laptop',
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'Name': 'Flat-screen',
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'Name': 'Table',
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }
    assert replacement_fee(inventory, 'laptop') == 4.0


def test_total_replacement_fee():
    cart = ['laptop', 'table']
    inventory = {
        'laptop': {
            'Name': 'Laptop',
            'In-stock': 16,
            'Rent': 12.0,
            'Value': 40.0
        },
        'flat-screen': {
            'Name': 'Flat-screen',
            'In-stock': 1,
            'Rent': 50.0,
            'Value': 100.0
        },
        'table': {
            'Name': 'Table',
            'In-stock': 4,
            'Rent': 10.0,
            'Value': 20.0
        }
    }

    assert total_replacement_fee(inventory, cart) == 6.0


def test_create_revenue_dictionary():
    revenue_dictionary = create_revenue_dictionary(['Revenue,0'])
    assert revenue_dictionary == {'Revenue': 0}


def test_add_revenue():
    revenue = {'Revenue': 1}
    assert add_revenue(revenue, 56) == {'Revenue': 57}


def test_subtract_revenue():
    revenue = {'Revenue': 57}
    assert subtract_revenue(revenue, 3) == {'Revenue': 54}

def test_create_revenue_string():
    revenue = {'Revenue': 1}
    assert create_revenue_string(revenue) == 'Revenue,1'