"""Module Scraper"""

import logging
from bs4 import BeautifulSoup

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.INFO)
logger = logging.getLogger('crawler')


class Scraper:
    def __init__(self, html:str):
        self.html = html
        self.soup = BeautifulSoup(self.html, "html.parser")

    def get_products_data(self): 
        products_data = []       
        logger.info('Start scraping data')
        products = self.soup.select("#product_list .s2 .list_brand.brand .brand-name > a")
        logger.debug('PRODUCTS: %s', products)
        
        for product in products:
            logger.debug('PRODUCT: %s', product)
            brand = product.select_one('.list_brand.brand')
            if brand is not None:
                brand_text = brand.text
                if brand_text == 'Lenovo':
                    a = product.select_one('.brand-name > a')               
                    href = a['href']
                    products_data.append(href)
            
        return products_data