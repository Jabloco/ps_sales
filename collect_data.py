from random import randint
from time import sleep


from html_parser import get_html, get_max_pages, get_product_details, get_products, get_html_selenium
from constants import BASE_URL, URL_REGION, URL_CATEGORY_ALL
from models import Product, Price


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
    page_html = get_html_selenium(url)
    if page_html:
        products_url = get_products(page_html)
    if products_url:
        return products_url
    return


def all_url_in_category(category_url:str) -> list:
    """
    Функция для получения всех ссылок в категории

    Принимаетсылку на категорию

    Возвращает список ссылок
    """
    all_products_in_category = []
    
    max_page = max_page_in_category(category_url)
    if max_page:
        for page in range(1, max_page + 1):
            page_url = f'{category_url}{str(page)}'
            sleep(randint(1, 5))
            products_on_page = products_url_on_page(page_url)
            if products_on_page:
                all_products_in_category.extend(products_on_page)
        return all_products_in_category
    return


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
            product_url = f'{BASE_URL}{url_product}'
            sleep(randint(1, 5))
            product_detail = get_product_details(get_html(product_url))
            print(product_detail)
            # parsed_title = product_detail['title']
            # parsed_description = product_detail['description']
            # parsed_url = url_product


if __name__ == '__main__':
    db_worker()
