""" Module Crawler """

import requests
import logging

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.INFO)
logger = logging.getLogger('crawler')

class Crawler:
    """
        Class retrieve HTML from a URL.
        https://www.jarcomputers.com/laptopi-cat-2.html
    """
    def __init__(self, url):
        self.url = url
        self.target_url = f'{self.url}'

    def get_html(self)->str:
        """get request
        """
        try:
            response = requests.get(self.target_url, timeout=8)
            if response.ok:
                html = response.text
                logger.debug('HTML: %s', html)
                logger.info('HTML is ready!')
                return html
            else:
                return "" 
        except requests.exceptions.RequestsException as e:
            logger.error(f"Failed to retrieve HTML from {self.target_url}:{e}")
            raise         