import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

from constants import HEADERS

def get_html(url):
    try:
        raw_html = requests.get(url, HEADERS)
        raw_html.raise_for_status()
        return raw_html.text
    except(requests.RequestException, ValueError):
        return


def get_sales(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    sales = (soup.find('div', class_='psw-m-t-6 psw-m-b-10')
                    .find('ul')
                    .find_all('li'))
    sales_links = [sale.find('a')['href'] for sale in sales]
    return sales_links


def get_pages(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    with open('raw_html.html', 'w', encoding='utf8') as f:
        f.write(raw_html)
    pages_ol = soup.find(attrs={'data-qa': 'ems-sdk-grid#ems-sdk-top-paginator-root#page...'}).text
    return pages_ol


def get_product(raw_html):
    product_data = {}
    soup = BeautifulSoup(raw_html, 'html.parser')

    # парсим имя игры
    product_name = soup.find(attrs={'data-qa': 'mfe-game-title#name'}).text
    product_data['title'] = product_name

    # цена на игру со скидкой
    try:
        price_final = soup.find(attrs={'data-qa': 'mfeCtaMain#offer0#finalPrice'}).text
    except AttributeError:
        price_final = None
    if price_final:
        product_data['price_final'] = price_final

    # обычная цена
    try:
        price_original = soup.find(attrs={'data-qa': 'mfeCtaMain#offer0#originalPrice'}).text
    except AttributeError:
        price_original = None
    if price_original:
        product_data['price_original'] = price_original

    # скидка для ps_plus?
    try:
        ps_plus_mark = soup.find('span', class_='psw-c-t-ps-plus psw-m-r-3').text
    except AttributeError:
        ps_plus_mark = None
    if ps_plus_mark:
        product_data['is_ps_plus_price'] = True

    producr_description = soup.find()

    return product_data
