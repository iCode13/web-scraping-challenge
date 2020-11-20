# Dependencies
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

import requests
import pandas as pd
import sys
sys.path.append('C:/Users/dbanerji/.virtualenvs/web-scraping-challenge-NSy6ynxU/lib/site-packages'
import pymongo

# Setup Mongo connection
CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.mars

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

