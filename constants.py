# import os

from db_settings import db_host, db_username, db_name, db_password

# basedir = os.path.abspath(os.path.dirname(__file__))
# DB_URI = 'sqlite:///' + os.path.join(basedir, 'psprice.sqlite3')

DB_URI = f'postgresql://{db_username}:{db_password}@{db_host}/{db_name}'

BASE_URL = 'https://store.playstation.com/'
URL_REGION = 'ru-ru/'
URL_CATEGORY_ALL = 'category/44d8bb20-653e-431e-8ad0-c0a365f68d2f/'

CHROME_DRIVER = './chromedriver'

API_URL = 'http://127.0.0.1:8000'
