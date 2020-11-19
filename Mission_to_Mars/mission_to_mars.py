# NASA Mars News
# Setup dependencies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

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
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
    driver.get(url_nasa)
    driver.implicitly_wait(wait)
    html_nasa = driver.page_source
    driver.close()
    
    return html_nasa

url_nasa = "https://mars.nasa.gov/news/"
html_nasa = get_html_nasa(url_nasa, wait=1)
soup_nasa = BeautifulSoup(html_nasa, "html.parser")

news_title = soup_nasa.find_all("div", class_="content_title")[1].text.strip()
news_p = soup_nasa.find_all("div", class_="article_teaser_body")[0].text.strip()

print("NASA Mars News Scrape")
print("-----------------------------------------")
print(news_title)
print(news_p)








