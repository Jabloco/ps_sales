from random import randint
from time import sleep


from store_parser.html_parser import get_html, get_sales, get_max_pages, get_product_details, get_products, get_html_selenium
from constants import BASE_URL, URL_REGION, URL_CATEGORY_ALL


def max_page_in_category_all(url:str) -> int:
    """
    Определяем максимальное число страниц в категории "Все игры"

    Принимает ссылку на категорию "Все игры"

    Selenium в headless режиме не всегда возвращает страницу, поэтому добавил проверку
    ограничением попыток = 5
    """
    max_pages = None
    retry_count = 0
    while max_pages is None and retry_count < 10:
        category_all_html = get_html_selenium(url)
        retry_count += 1
        if category_all_html:
            max_pages = get_max_pages(category_all_html)
    if max_pages:
        return int(max_pages)
    return


def products_on_page_url(url:str) -> list:
    page_html = None
    retry_count = 0
    while page_html is None and retry_count < 10:
        sleep(randint(1, 5))
        page_html = get_html_selenium(url)
        retry_count += 1
        print(retry_count)
        if page_html:
            products_url = get_products(page_html)
    if products_url:
        return products_url
    return

if __name__ == '__main__':
    """
    Пайплайн в общем виде:
        заходим на страницу категории
        получаем максимальное число страниц в категории
        циклом проходим по всем страницам категории
        с каждой страницы собираем ссылки на продукты, пишем их в писок
        проходим по спику подуктов и парсим подробности, пишем данные в базу
    """
    category_all_url = BASE_URL + URL_REGION + URL_CATEGORY_ALL

    max_page = max_page_in_category_all(category_all_url)
    if max_page:
        all_products_in_category = []
        for page in range(1, max_page + 1):
            sleep(randint(1, 5))
            page_url = f'{category_all_url}{str(page)}'
            print(page_url)
            products_on_page = products_on_page_url(page_url)
            if products_on_page:
                all_products_in_category.extend(products_on_page)
            print(all_products_in_category)
            print(len(all_products_in_category))

