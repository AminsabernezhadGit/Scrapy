from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")  # Use this argument to run in headless mode
options.add_argument("--window-size=1920,1200")

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

driver.get("https://dartil.com/collection/cat-mobile/")

PRODUCTS = driver.find_elements(By.CSS_SELECTOR, "h3")

for product in PRODUCTS:
    print(product.text)

driver.quit()
