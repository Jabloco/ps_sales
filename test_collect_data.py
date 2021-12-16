from collect_data import write_to_db

def test_write_to_db_product_not_in_db():
    product_detail = {
        'title': 'Name1',
        'price_final': '1000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == (False, f"Price final {product_detail['price_final']}, price original {product_detail['price_original']}")


def test_write_to_db_produtct_in_db():
    product_detail = {
        'title': 'Name1',
        'price_final': '1000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == None

def test_write_to_db_price_update():
    product_detail = {
        'title': 'Name1',
        'price_final': '2000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == (True, f"Price final {product_detail['price_final']}, price original {product_detail['price_original']}")

def test_write_to_db_price_update_2():
    product_detail = {
        'title': 'Name1',
        'price_final': '2000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == (True, f"Price final {product_detail['price_final']}, price original {product_detail['price_original']}")

def test_write_to_db_price_update_3():
    product_detail = {
        'title': 'Name1',
        'price_final': '3000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == (True, f"Price final {product_detail['price_final']}, price original {product_detail['price_original']}")