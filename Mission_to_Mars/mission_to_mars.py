# Setup dependencies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pandas as pd

# NASA Mars News scrape for latest news and teaser text
# # Use Selenium to scrape NASA Mars News
def get_html_nasa(url_nasa, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
    driver.get(url_nasa)
    driver.implicitly_wait(wait)
    html_nasa = driver.page_source
    driver.close()
    
    return html_nasa

url_nasa = "https://mars.nasa.gov/news/"
html_nasa = get_html_nasa(url_nasa, wait=5)
soup_nasa = BeautifulSoup(html_nasa, "html.parser")

news_title = soup_nasa.find_all("div", class_="content_title")[1].text.strip()
news_p = soup_nasa.find_all("div", class_="article_teaser_body")[0].text.strip()

print("Latest NASA Mars News")
print("-------------------------")
print(news_title)
print(news_p)

# JPL Mars Space Images
# Visit the url for JPL Featured Space Image here
def get_html_jpl(url_jpl, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
    driver.get(url_jpl)
    driver.implicitly_wait(wait)
    html_jpl = driver.page_source
    driver.close()
    
    return html_jpl

url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
html_jpl = get_html_jpl(url_jpl, wait=5)
soup_jpl = BeautifulSoup(html_jpl, "html.parser")

image_url = soup_jpl.find('a', class_="button fancybox")["data-fancybox-href"]
featured_image_url = "https://www.jpl.nasa.gov" + image_url

print("JPL Mars Space Images - Featured Image")
print("-------------------------------------------")
print(featured_image_url)






