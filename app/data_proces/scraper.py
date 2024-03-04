"""Module Scraper"""

from bs4 import BeautifulSoup
import logging

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.DEBUG)
logger = logging.getLogger('scraper')

class Scraper:
    def __init__(self,html):
        self.soup = BeautifulSoup(html,"html.parser")  

    def get_products_urls(self):
        products_urls = []

        logger.info('Start scraping data')
        products_selector = "#product_list.p1 .s2"

        products = self.soup.select(products_selector)
        logger.debug('PRODUCTS: %s', products)
        for product in products:
            logger.debug('PRODUCT: %s', product)
            brand = product.select_one(".list_brand.brand")

            if brand == 'Lenovo':
                a = product.select_one("a.brand-name")
                href = a['href']
                products_urls.append(href)
        return products_urls         