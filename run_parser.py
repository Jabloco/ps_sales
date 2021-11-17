from html_parser import get_html, get_sales
from constants import BASE_URL, URL_REGION

sales_url = BASE_URL + URL_REGION + 'pages/deals'
raw_html = get_html(sales_url)
if raw_html:
    print(get_sales(raw_html))
