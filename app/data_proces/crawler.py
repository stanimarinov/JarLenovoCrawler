"""This module contains the Crawler class for retrieving HTML content from a URL."""

import os
import requests
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class CrawlerError(Exception):
    """Custom exception for errors related to Crawler."""

    def __init__(self, message):
        super().__init__(message)

class Crawler:
   """A class for retrieving HTML content from a URL.
       This class provides methods for fetching HTML content from a given URL and saving it to a file.
   """
   def __init__(self, url):
       self.target_url = url
   def save_to_file(self, html, filename="../data/content.html"):
       """Save the HTML content to a file."""
       os.makedirs(os.path.dirname(filename), exist_ok=True)
       with open(filename, 'w', encoding="utf-8") as f:
           f.write(html)
   def get_html(self):
       """Retrieves the HTML content of a given URL."""
       
       user_agent = "A scrapper for learning"
       headers = {"User-Agent": user_agent}
       
       try:
           response = requests.get(self.target_url, headers=headers, timeout=5)
           response.raise_for_status()  
           logger.debug('Response: %s', response.text)
           response.encoding = "utf-8"
           logger.info('HTML retrieved!')
           return response.text
       except requests.exceptions.RequestException as e:
           logger.error("Failed to retrieve HTML from %s: %s", self.target_url, e)
           raise 

if __name__=="__main__":
   target_url = 'https://www.jarcomputers.com/laptopi-cat-2.html'
   crawler = Crawler(target_url)
   html = crawler.get_html()
   crawler.save_to_file(html=html)
             