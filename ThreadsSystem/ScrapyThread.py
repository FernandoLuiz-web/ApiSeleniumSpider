from threading import Thread
import _thread
from Utils import Exception
import os


class SpiderThread(Thread):
    name = ''
    url = ''
    spider_path = "C:\\Users\\Luiz Fernando\\Documents\\APISelenium\\Spiders"

    def __init__(self, name, url):
        self.name = name
        self.url = url
        createSpider(name, self.spider_path)
        _thread.start_new_thread(GenerateSpider(name, url))


def createSpider(name, spider_path):

    os.chdir(spider_path)
    try:
        if not os.path.isdir(f'{name}Scrapy'):
            os.system(f'scrapy startproject {name}Scrapy')
        else:
            raise Exception.Error_in_execution_time('spider_exists')
    except:
        raise Exception.Error_in_execution_time('thread_Spider')


def GenerateSpider(name, url):
    gen_spider_file = f"C:\\Users\\Luiz Fernando\\Documents\\APISelenium\\Spiders\\{name}Scrapy\\{name}Scrapy\\spiders\\{name}.py"
    gen_spider_path = f"C:\\Users\\Luiz Fernando\\Documents\\APISelenium\\Spiders\\{name}Scrapy"
    try:
        os.chdir(gen_spider_path)
        if not os.path.isfile(gen_spider_file):
            os.system(f'scrapy genspider {name} {url}')
        else:
            raise Exception.Error_in_execution_time('spider_exists')
    except:
        raise Exception.Error_in_execution_time('thread_Spider')