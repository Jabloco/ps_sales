import requests

from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

from constants import CHROME_DRIVER

def get_html(url):
    """
    Функция получает ссылку и возвращает html-код.

    Используем для статических страниц, ибо работает сильно быстрее selenium
    """
    try:
        raw_html = requests.get(url)
        raw_html.raise_for_status()
    except RequestException:
        return
    return raw_html.text


def get_html_selenium(url):
    """
    Функция получает ссылку и возвращает html-код.

    Используется selenium и его возможность запуска без итерфейса (--headless)

    Есть смысл использовать данную функцию только для динамических страниц

    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')
    try:
        browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_DRIVER)
        browser.get(url)
    except WebDriverException:
        return
    raw_html = browser.page_source
    return raw_html


def get_sales(raw_html):
    """
    Функция для получения ссылок на распродажи.

    Получает html, возвращает список ссылок на распродажи
    """
    soup = BeautifulSoup(raw_html, 'html.parser')
    try:
        sales = (soup.find('div', class_='psw-m-t-6 psw-m-b-10')
                    .find('ul')
                    .find_all('li')
                )
    except AttributeError:
        return
    sales_links = [sale.find('a')['href'] for sale in sales]
    return sales_links


def get_pages(raw_html):
    """
    Функция для нахождения максимального числа страниц в магазине.

    Принимает html

    Возвращает последнее число из пагинатора
    """
    soup = BeautifulSoup(raw_html, 'html.parser')
    try:
        pages_li = (soup.find(attrs={'data-qa': 'ems-sdk-bottom-paginator-root'})
                        .find('ol')
                        .find_all('li')
                    )
    except AttributeError:
        return
    try:
        pages = [page.find('button')['value'] for page in pages_li]
    except UnboundLocalError:
        return
    return int(pages[-1])


def get_product(raw_html):
    """
    Получение данных о продукте.

    Принимает html

    Возвращает словарь с данными
    """
    product_data = {}
    soup = BeautifulSoup(raw_html, 'html.parser')

    # парсим имя игры
    try:
        product_name = soup.find(attrs={'data-qa': 'mfe-game-title#name'}).text
    except AttributeError:
        product_name = None
    product_data['title'] = product_name

    # цена на игру со скидкой
    try:
        price_final = soup.find(attrs={'data-qa': 'mfeCtaMain#offer0#finalPrice'}).text
    except AttributeError:
        price_final = None
    product_data['price_final'] = price_final

    # обычная цена
    try:
        price_original = soup.find(attrs={'data-qa': 'mfeCtaMain#offer0#originalPrice'}).text
    except AttributeError:
        price_original = None
    product_data['price_original'] = price_original

    # скидка для ps_plus?
    try:
        ps_plus_mark = soup.find('span', class_='psw-c-t-ps-plus psw-m-r-3').text
    except AttributeError:
        ps_plus_mark = None
    if ps_plus_mark:
        is_ps_plus_price = True
    else:
        is_ps_plus_price = False
    product_data['is_ps_plus_price'] = is_ps_plus_price

    # описание продукта
    try:
        product_description = soup.find(attrs={'data-qa': 'mfe-game-overview#description'}).text
    except AttributeError:
        product_description = None
    product_data['description'] = product_description

    return product_data