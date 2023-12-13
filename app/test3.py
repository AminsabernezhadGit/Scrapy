import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class DartilSpider(scrapy.Spider):
    name = 'easy'
    start_urls = ['https://dartil.com/collection/cat-mobile/']

    def __init__(self, *args, **kwargs):
        super(DartilSpider, self).__init__(*args, **kwargs)

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1200")

        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    def parse(self, response):
        self.driver.get(response.url)

        # Wait for some time if necessary for the page to load (you might need to customize this)
        self.driver.implicitly_wait(5)

        # Use Scrapy Selector to parse the HTML
        selector = Selector(text=self.driver.page_source)

        # Extract data
        products = selector.css("h3::text").getall()

        # Print or yield the data as needed
        for product in products:
            print(product)

        self.driver.quit()
