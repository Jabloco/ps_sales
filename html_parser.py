import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_html(url):
    try:
        raw_html = requests.get(url)
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


def get_product(raw_html):
    pass

