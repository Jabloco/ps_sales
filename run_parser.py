from store_parser.html_parser import get_html, get_sales, get_max_pages, get_product_details, get_products, get_html_selenium
from constants import BASE_URL, URL_REGION, URL_CATEGORY_ALL


def max_page_in_category_all(url):
    """
    Определяем максимальное число страниц в категории "Все игры"

    Принимает ссылку на категорию "Все игры"
    
    Selenium в headless режиме не всегда возвращает страницу, поэтому добавил проверку
    ограничением попыток = 5
    """
    max_pages = None
    retry_count = 0
    while max_pages is None and retry_count < 5:
        category_all_html = get_html_selenium(url)
        retry_count += 1
        if category_all_html:
            max_pages = get_max_pages(category_all_html)
    if max_pages:
        return int(max_pages)
    return


if __name__ == '__main__':
    category_all_url = BASE_URL + URL_REGION + URL_CATEGORY_ALL

    max_page = max_page_in_category_all(category_all_url)
    if max_page:
        for page in range(1, max_page + 1):
            print(category_all_url + str(page))

