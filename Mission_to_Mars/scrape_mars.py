from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import pandas as pd
from pprint import pprint

# Setup Selenium driver
def driver_setup():
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")

    return driver

# Define scrape function for scraping data
def scrape(driver):
    mars_dict = {}
    # Latest NASA News
    url_news = "https://mars.nasa.gov/news/"
    driver.get(url_news)
    driver.implicitly_wait(5)
    html_news = driver.page_source
    soup_news = bs(html_news, "html.parser")

    news_title = soup_news.find_all("div", class_="content_title")[0].text.strip()
    if not len(soup_news.find_all("div", class_="list_text")):
        print("empty array")
    news_p = soup_news.find_all("div", class_="list_text")[0].text.strip()
    mars_dict['news_title'] = news_title
    mars_dict['news_paragraph'] = news_p

    # Featured Mars Images
    url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    driver.get(url_jpl)
    driver.implicitly_wait(5)
    html_jpl = driver.page_source
    soup_jpl = bs(html_jpl, "html.parser")

    image_url = soup_jpl.find('a', class_="button fancybox")["data-fancybox-href"]
    featured_image_url = "https://www.jpl.nasa.gov" + image_url
    mars_dict['featured_image'] = featured_image_url

    # Mars Facts
    url_facts = "https://space-facts.com/mars/"
    facts_scrape = pd.read_html(url_facts)
    df_facts = pd.DataFrame(facts_scrape[0])
    df_facts.columns = ['Description', 'Mars']    
    html_facts = df_facts.to_html(header = False, index = False)
    mars_dict['facts'] = html_facts

    # Mars Hemipheres
    url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    driver.get(url_hemisphere)
    driver.implicitly_wait(5)
    html_hemisphere = driver.page_source
    soup_hemisphere = bs(html_hemisphere, "html.parser")
    
    outputs = soup_hemisphere.find_all('div', class_='item')
    hemisphere_image_urls=[]
    for output in outputs:
        title = output.find('h3').text
        end_url = output.a['href']
        x = end_url.replace('search/map','download')
        dict = {}
        dict['title'] = title
        dict['img_url'] = "https://astropedia.astrogeology.usgs.gov" + x + ".tif/full.jpg"
        hemisphere_image_urls.append(dict)
    mars_dict['hemisphere_image'] = hemisphere_image_urls

    return mars_dict
    driver.close()
    
driver = driver_setup()
# pprint(scrape(driver))








