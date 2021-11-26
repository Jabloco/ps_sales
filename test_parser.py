from store_parser.html_parser import get_html, get_sales, get_max_pages, get_product_details, get_products, get_html_selenium
from constants import BASE_URL, URL_REGION, URL_CATEGORY_ALL

# sales_url = BASE_URL + URL_REGION + 'pages/deals'
# sales_html = get_html(sales_url)
# if sales_html:
#     print(get_sales(sales_html))

category_url = BASE_URL + URL_REGION + URL_CATEGORY_ALL + '1'
print(category_url)
category_html = get_html_selenium(category_url)
if category_html:
    # print(get_max_pages(category_html))
    print(get_products(category_html))

# product_url = 'https://store.playstation.com/ru-ru/product/EP4133-CUSA17124_00-AEONMUSTDIE00000'

# product_html = get_html(product_url)
# if product_html:
#     print(get_product_details(product_html))
