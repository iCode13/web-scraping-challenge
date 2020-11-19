# Setup dependencies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Use Selenium to grab html
def get_html(url, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
    driver.get(url)
    driver.implicitly_wait(wait)
    html = driver.page_source
    driver.close()
    
    return html

# Page to be scraped - NASA Mars News
def get_html_nasa(url_nasa, wait):
    #fireFoxOptions = webdriver.FirefoxOptions()
    options = Options()
    options.headless = True
    # fireFoxOptions.set_headless()
    # driver = webdriver.Firefox("C:/Program Files/Mozilla Firefox/geckodriver.exe")
    driver = webdriver.Firefox(options=options, executable_path=r'driver/geckodriver.exe')
    driver.get(url_nasa)
    driver.implicitly_wait(wait)
    html_nasa = driver.page_source
    browser.close()
    
    return html_nasa



