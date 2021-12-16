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
    assert write_to_db(product_detail, None) == (False, 'Price final 1000, price original None')


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