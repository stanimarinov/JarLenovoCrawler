""" Module: process """

import logging

from crawler import Crawler
from scraper import Scraper


if __name__=='__main__':
    url = 'https://www.jarcomputers.com/Laptopi_cat_2.html'

    crawler = Crawler(url)
    html = crawler.get_html()

    scraper = Scraper(html)
    scraper.get_products_data()