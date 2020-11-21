import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pymongo
import time

# Setup Mongo connection
CONN = os.getenv("CONN")
client = pymongo.MongoClient(CONN)
db = client.mars

# Create Mars data dict for inserting into mongoDB
mars_dict = {}

# # NASA Mars News
# def get_html_news(url_news, wait):
#     fireFoxOptions = webdriver.FirefoxOptions()
#     fireFoxOptions.set_headless()
#     driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
#     driver.get(url_news)
#     driver.implicitly_wait(wait)
#     html_news = driver.page_source
#     driver.close()
    
#     return html_news

# url_news = "https://mars.nasa.gov/news/"
# html_news = get_html_news(url_news, wait=5)
# soup_news = bs(html_news, "html.parser")
# news_title = soup_news.find_all("div", class_="content_title")[1].text.strip()
# news_p = soup_news.find_all("div", class_="list_text")[0].text.strip()
# news = [news_title, news_p]
# mars_dict['news'] = news

# # JPL Mars Space Images
# def get_html_jpl(url_jpl, wait):
#     fireFoxOptions = webdriver.FirefoxOptions()
#     fireFoxOptions.set_headless()
#     driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
#     driver.get(url_jpl)
#     driver.implicitly_wait(wait)
#     html_jpl = driver.page_source
#     driver.close()
    
#     return html_jpl

# url_jpl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
# html_jpl = get_html_jpl(url_jpl, wait=5)
# soup_jpl = bs(html_jpl, "html.parser")
# image_url = soup_jpl.find('a', class_="button fancybox")["data-fancybox-href"]
# featured_image_url = "https://www.jpl.nasa.gov" + image_url
# mars_dict['featured_image'] = featured_image_url

# # Mars Facts
# url_facts = "https://space-facts.com/mars/"
# facts_scrape = pd.read_html(url_facts)
# df_facts = pd.DataFrame(facts_scrape[0])
# df_facts.columns = ['Description', 'Mars']    
# df_facts = df_facts.set_index('Description')
# html_facts = df_facts.to_html(header = False, index = False)
# mars_dict['facts'] = html_facts

# # Mars Hemipheres
# def get_html_hemisphere(url_hemisphere, wait):
#     fireFoxOptions = webdriver.FirefoxOptions()
#     fireFoxOptions.set_headless()
#     driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
#     driver.get(url_hemisphere)
#     driver.implicitly_wait(wait)
#     html_hemisphere = driver.page_source
#     driver.close()
#     return html_hemisphere

# url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
# html_hemisphere = get_html_hemisphere(url_hemisphere, wait = 5)
# soup_hemisphere = bs(html_hemisphere, "html.parser")
# outputs = soup_hemisphere.find_all('div', class_='item')
# hemisphere_image_urls=[]
# for output in outputs:
#     title = output.find('h3').text
#     end_url = output.a['href']
#     x = end_url.replace('search/map','download')
#     dict = {}
#     dict['title'] = title
#     dict['image_url'] = "https://astropedia.astrogeology.usgs.gov" + x + ".tif/full.jpg"
#     hemisphere_image_urls.append(dict)
# mars_dict['hemisphere_image'] = hemisphere_image_urls

# print(mars_dict)


# # # Use Selenium to grab html
# # def get_html(url, wait):
# #     fireFoxOptions = webdriver.FirefoxOptions()
# #     fireFoxOptions.set_headless()
# #     driver = webdriver.Firefox(
# #         options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
# #     driver.get(url)
# #     driver.implicitly_wait(wait)
# #     html = driver.page_source
# #     driver.close()

# #     return html

# # # Define function to scrape the four url's
# # def scrape():
# #     url = "https://mars.nasa.gov/news/"
# #     html = get_html(url, wait=5)
# #     soup = bs(html, 'html.parser')
# #     news_title = soup.find_all("div", class_="content_title")[1].text.strip()
# #     news_p = soup.find_all("div", class_="list_text")[1].text.strip()
# #     news = [news_title, news_p]
# # mars_dict['news'] = news
   
# #     url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
# #     html = get_html(url, wait=5)
# #     soup = bs(html, "html.parser")
# #     image_url = soup.find('a', class_="button fancybox")["data-fancybox-href"]
# #     featured_image_url = "https://www.jpl.nasa.gov" + image_url
# # mars_dict['featured_image'] = featured_image_url
    
# #     url_facts = "https://space-facts.com/mars/"
# #     facts_scrape = pd.read_html(url_facts)
# #     df_facts = pd.DataFrame(facts_scrape[0])
# #     df_facts.columns = ['Description', 'Mars']
# #     df_facts = df_facts.set_index('Description')
# #     html_facts = df_facts.to_html(header=False, index=False)
# # mars_dict['facts'] = html_facts
  
# #     url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
# #     html = get_html(url, wait=5)
# #     soup = bs(html, "html.parser")
# #     outputs = soup.find_all('div', class_='item')
# #     hemisphere_image_urls = []
# #     for output in outputs:
# #         title = output.find('h3').text
# #         end_url = output.a['href']
# #         x = end_url.replace('search/map', 'download')
# #         dict = {}
# #         dict['title'] = title
# #         dict['image_url'] = "https://astropedia.astrogeology.usgs.gov" + x + ".tif/full.jpg"
# #         hemisphere_image_urls.append(dict)
# # mars_dict['hemisphere_image'] = hemisphere_image_urls
    
# # print(mars_dict)
