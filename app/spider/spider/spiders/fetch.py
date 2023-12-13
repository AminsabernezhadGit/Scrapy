import scrapy
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Add this line for sending keys


class DriverFetch(scrapy.Spider):
    name = 'easy'

    def __init__(self, *args, **kwargs):
        super(DriverFetch, self).__init__(*args, **kwargs)

        self.start_urls = kwargs.get('start_urls', [])
        self.css_price_selector = kwargs.get('css_price_selector', '')
        self.css_color_selector = kwargs.get('css_color_selector', '')

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1200")

        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.implicitly_wait(5)

        # Extract color elements
        color_elements = self.driver.find_elements(By.CSS_SELECTOR, self.css_color_selector)

        for color_element in color_elements:
            # Click on the color element
            color_element.click()

            products = self.driver.find_elements(By.CSS_SELECTOR, self.css_price_selector)

            product_texts = [product.text for product in products]

            # Print or yield the data as needed
            for product_text in product_texts:
                print(f"color: {color_element.text} ===> price: {product_text}")

        self.driver.quit()
