from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.settings import HEADLESS

def init_driver():
    options = ChromeOptions()
    if HEADLESS:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver