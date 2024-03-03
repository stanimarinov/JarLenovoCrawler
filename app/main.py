from app_proces.crawler import Crawler
from app_proces.scraper import Scraper

if __name__=='__main__':
    url = 'https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1'

    crawler = Crawler(url)
    html = crawler.get_html()

    scraper = Scraper(html)
    scraper.get_products_urls()