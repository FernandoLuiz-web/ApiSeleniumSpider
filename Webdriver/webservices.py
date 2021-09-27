from Utils import Exception
from selenium import webdriver
from playwright.sync_api import sync_playwright


class WebService:

    @staticmethod
    def Selenium_site(url):
        try:
            browser = webdriver.Chrome()
            browser.get(url)
            title = browser.title
            browser.quit()
            return {
                'Title': title
            }
        except:
            raise Exception.Error_in_execution_time('runtime')

    @staticmethod
    def Playwright_site(url):
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto(url)
                title = page.title()
                browser.close()
                return {
                    'Title': title
                }
        except:
            raise Exception.Error_in_execution_time('runtime')
