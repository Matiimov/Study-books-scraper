import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.books import BooksSpider

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(BooksSpider)
    process.start()
