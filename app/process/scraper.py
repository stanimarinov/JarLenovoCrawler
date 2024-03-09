"""Module Scraper"""

import logging
from bs4 import BeautifulSoup

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.INFO)
logger = logging.getLogger('scraper')


class Scraper:
    def __init__(self, html:str):
        self.html = html
        self.soup = BeautifulSoup(self.html, "html.parser")

    
    def get_products_urls(self):
        products_urls = []

        logger.info('Start scraping data')
        products = self.soup.select('#product_list .brand-name')
        logger.debug('PRODUCTS: %s', products)

        for product in products:
            brand = product.select_one('.brand-name>a')
            logger.info('PRODUCT: %s', product)

            if brand and brand.text == 'Lenovo':
                href = product.find('a')['href']
                products_urls.append(href)
                
        return products_urls