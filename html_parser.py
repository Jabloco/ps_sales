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


def get_pages(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    with open('raw_html.html', 'w', encoding='utf8') as f:
        f.write(str(soup))
    pages_li = soup.find_all('button', class_='psw-button')
    return pages_li


def get_product(raw_html):
    product_data = {}
    soup = BeautifulSoup(raw_html, 'html.parser')
    product_name = (soup.find('main', class_='pdp-main psw-dark-theme')
                        .find('div', class_='psw-l-stack-left psw-fill-x')
                        .find('div', class_='psw-l-anchor psw-l-z-1 psw-l-grid psw-l-gap-y-7')
                        .find('div', class_='psw-pdp-card-anchor psw-l-stack-bottom psw-l-w-1/1 psw-l-w-5/12@tablet-s psw-l-w-1/3@tablet-l psw-l-w-1/3@laptop psw-l-w-7/24@desktop psw-l-w-7/24@max psw-p-x-5@below-tablet-s')
                        .find('div', class_='psw-c-bg-card-1 psw-p-y-7 psw-p-x-8 psw-m-sub-x-8 psw-m-sub-x-6@below-tablet-s psw-p-x-6@below-tablet-s')
                        .find('div', class_='pdp-game-title')
                        .find('div', class_='psw-root psw-dark-theme')
                        .find('h1', class_='psw-m-b-5 psw-t-title-l psw-t-size-8 psw-l-line-break-word').text
    )
                    
    product_data['name'] = product_name

    return product_data