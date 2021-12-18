from collect_data import write_to_db

def test_write_to_db_product_not_in_db():  # продукта нет в базе
    product_detail = {
        'title': 'Name1',
        'price_final': '1000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == (False, f"Price final {product_detail['price_final']}, price original {product_detail['price_original']}")


def test_write_to_db_produtct_in_db():  # повторно приходят те же данные
    product_detail = {
        'title': 'Name1',
        'price_final': '1000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == None

def test_write_to_db_price_update():  # пробуем обновить цену
    product_detail = {
        'title': 'Name1',
        'price_final': '2000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == (True, f"Price final {product_detail['price_final']}, price original {product_detail['price_original']}")

def test_write_to_db_price_update_2():  # пробуем обновить цену предыдущей ценой
    product_detail = {
        'title': 'Name1',
        'price_final': '2000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == None

def test_write_to_db_price_update_3():  # пробуем обновить цену другой ценой
    product_detail = {
        'title': 'Name1',
        'price_final': '1000',
        'price_original': None,
        'url': '/ru/name1',
        'is_ps_plus_price': False,
        'description': 'Text'
    }
    assert write_to_db(product_detail, None) == (True, f"Price final {product_detail['price_final']}, price original {product_detail['price_original']}")