import scrapy


class SiteSpider(scrapy.Spider):
    name = 'Site'
    allowed_domains = ['https://www.jw.org/pt/biblioteca/biblia/biblia-de-estudo/livros/salmos/46/']
    start_urls = ['http://https://www.jw.org/pt/biblioteca/biblia/biblia-de-estudo/livros/salmos/46//']

    def parse(self, response):
        pass
