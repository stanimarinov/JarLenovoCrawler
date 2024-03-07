""" Module: data_proces """
import logging
from typing import List

from crawler import Crawler
from scraper import Scraper, ScraperError
from app.db.db import DB
from types import LenovoData
from app.setup_logging import setup_logger

logger = setup_logger('data_proces', logging.DEBUG)

class DataProces:
    def __init__(self, target_url: str):
        """ Initialize  DataProces """

        self.target_url = target_url
        self.db = DB(config_file='app/config.ini', section='mysql')

    def scrape_data(self) -> List[LenovoData]:
        """ Scrape data from the target URL. """
        crawler = Crawler(self.target_url)

        html = crawler.get_html()

        scraper = Scraper(html)
        try:
            laptop_data = scraper.get_laptop_data()
        except ScraperError as e:
            logger.error('Error scraping data: %s', e)

        logger.debug(laptop_data[:10])
        logger.info('Fetched %s laptop data', len(laptop_data))

        return laptop_data

    def insert_data(self, data: List[LenovoData]) -> None:
        """ Insert data into database. """

        self.db.insert_laptop_data(data)

    def run(self):
        """ Run data proces """
        data = self.scrape_data()
        self.insert_data(data)