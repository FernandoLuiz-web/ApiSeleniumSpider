import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top/?ref=nv_mv_250']

    def parse(self, response):
        for films in response.css('.titleColumn'):
            titles = response.css('.titleColumn a ::text')
            age = response.css('.secondaryInfo ::text')
            evaluation = response.css('strong ::text')
        pass
