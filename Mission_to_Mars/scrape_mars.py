# Dependencies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# For Latest NASA Mars News
def get_html_news(url_news, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
    driver.get(url_news)
    driver.implicitly_wait(wait)
    html_news = driver.page_source
    driver.close()
    
    return html_news

def scrape():
    url_news = 'https://mars.nasa.gov/news/'
    html_news = get_html_news(url_news, wait=5)
    soup_news = bs(html_news,'html.parser')
    
    news_title = soup_news.find_all("div", class_="content_title")[1].text.strip()
    news_p = soup_news.find_all("div", class_="list_text")[0].text.strip()
    
    listings = {}
    listings['news_title'] = news_title
    listings['news_p'] = news_p
    
    print(news_title)
    print(news_p)
