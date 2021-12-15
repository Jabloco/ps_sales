from random import randint
from time import sleep
from datetime import date


from html_parser import get_html, get_max_pages, get_product_details, get_products, get_html_selenium
from constants import BASE_URL, URL_REGION, URL_CATEGORY_ALL
from models import Product, Price
from sqlalchemy import desc


def max_page_in_category(url: str) -> int:
    """
    Определяем максимальное число страниц в категории

    Принимает ссылку на категорию. Возвращает число.
    """
    category_all_html = get_html_selenium(url)
    if category_all_html:
        max_pages = get_max_pages(category_all_html)
    if max_pages:
        return int(max_pages)
    return


def products_url_on_page(url: str) -> list:
    """
    Функция получения ссылок на продукты со страницы категории.

    Принимает ссылку на страницу категории, возвращает список ссылок.
    """
    # увеличил время в get_html_selenium
    # нужно добавить проверку
    page_html = get_html_selenium(url)
    if page_html:
        products_url = get_products(page_html)
    if products_url:
        return products_url
    return


def all_url_in_category(category_url: str) -> list:
    """
    Функция для получения всех ссылок в категории

    Принимаетсылку на категорию

    Возвращает список ссылок
    """
    all_products_in_category = []

    max_page = max_page_in_category(category_url)
    if max_page:
        for page in range(1, 3):
            page_url = f'{category_url}{str(page)}'
            sleep(randint(1, 5))
            products_on_page = products_url_on_page(page_url)
            if products_on_page:
                all_products_in_category.extend(products_on_page)
        return all_products_in_category
    return


def check_product_in_db(url_product):
    """
    Функция для проверки наличия продукта в БД

    Возвращает метку наличия, если продукта нет в БД то еще возвращает детали о продукте
    """
    product_url = f'{BASE_URL}{url_product}'
    is_product_in_db = Product.query.filter_by(url=url_product).first()
    if is_product_in_db is None:
        sleep(randint(1, 5))
        product_detail = get_product_details(get_html(product_url))
        product_detail['url'] = url_product
        return False, product_detail
    return True, None

# между этими функциями логическая не состыковка

def write_to_db(is_product_in_db, product_detail):
    """
    Функция записи данных в БД

    Принимает метку наличия продуката в базе и детали продукта
    """
    if is_product_in_db is None:
        parsed_title = product_detail['title']
        parsed_description = product_detail['description']
        parsed_url = product_detail['url']
        product = Product.insert(
            parsed_title,
            parsed_description,
            parsed_url
        )

    prices = Price.query.filter_by(id_product=product.id).order_by(desc(Price.date_change)).first()
    parsed_price_final = product_detail['price_final']
    parsed_price_original = product_detail['price_final']
    parsed_ps_plus_price = product_detail['is_ps_plus_price']
    date_change = date.today()

    if prices is None:
        price_obj = Price.insert(
            product.id,
            parsed_price_final,
            parsed_price_original,
            parsed_ps_plus_price,
            date_change
        )
        print (price_obj)
        return False, price_obj
    elif prices.price_final != parsed_price_final or prices.price_original != parsed_price_original:
        price_obj = Price.insert(
            product.id,
            parsed_price_final,
            parsed_price_original,
            parsed_ps_plus_price,
            date_change
        )
        return True, price_obj

def db_worker():
    """
    Пайплайн в общем виде:
        заходим на страницу категории
        получаем максимальное число страниц в категории
        циклом проходим по всем страницам категории
        с каждой страницы собираем ссылки на продукты, пишем их в писок
        проходим по спику подуктов и парсим подробности, пишем данные в базу
    """
    category_all_url = BASE_URL + URL_REGION + URL_CATEGORY_ALL

    url_in_category = all_url_in_category(category_all_url)

    if url_in_category:
        for url_product in url_in_category:
            is_product_in_db, product_detail = check_product_in_db(url_product)
            write_to_db(is_product_in_db, product_detail)


if __name__ == '__main__':
    db_worker()
