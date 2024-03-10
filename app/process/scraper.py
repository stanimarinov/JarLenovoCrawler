"""Module Scraper"""

import requests
from bs4 import BeautifulSoup
import logging

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.INFO)
logger = logging.getLogger('scraper')

url = 'https://www.jarcomputers.com/Laptopi_cat_2.html'

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
            logger.debug('PRODUCT: %s', product)
            if brand and brand.text == 'Lenovo':
                href = product.find('a')['href']
                products_urls.append(href)                
        return products_urls
    
page = requests.get(url) 
soup = BeautifulSoup(page.content, "html.parser") 
products = soup.find_all('a') 
text = 'Lenovo'
 
for product in products:
    if(product.string == text):
        print(product)