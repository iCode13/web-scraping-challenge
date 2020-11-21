# Setup dependencies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import pandas as pd


# NASA Mars News scrape for latest news and teaser text
# Use Selenium to scrape NASA Mars News
def get_html_news(url_news, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
    driver.get(url_news)
    driver.implicitly_wait(wait)
    html_news = driver.page_source
    driver.close()
    
    return html_news

url_news = "https://mars.nasa.gov/news/"
html_news = get_html_news(url_news, wait=5)
soup_news = bs(html_news, "html.parser")

# Write scraped html to file
with open('html_news_dump.html', 'w+', encoding='utf-8') as f:
    f.write(html_news)

news_title = soup_news.find_all("div", class_="content_title")[1].text.strip()
news_p = soup_news.find_all("div", class_="list_text")[1].text.strip()

print("***********************")
print("Latest NASA Mars News")
print("***********************")
print(news_title)
print(news_p)


# JPL Mars Space Images
# Use Selenium to scrape JPL Featured Space Image
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
soup_jpl = bs(html_jpl, "html.parser")

# Write scraped html to file
with open('html_jpl_dump.html', 'w+', encoding='utf-8') as f:
    f.write(html_jpl)

image_url = soup_jpl.find('a', class_="button fancybox")["data-fancybox-href"]
featured_image_url = "https://www.jpl.nasa.gov" + image_url

print("****************************************")
print("JPL Mars Space Images - Featured Image")
print("****************************************")
print(featured_image_url)


# Mars Facts
# Data scraping with pandas
url_facts = "https://space-facts.com/mars/"
facts_scrape = pd.read_html(url_facts)

# Add scraped data to dataframe
df_facts = pd.DataFrame(facts_scrape[0])
df_facts.columns = ['Description', 'Mars']    
df_facts = df_facts.set_index('Description')

# Display HTML table string
html_facts = df_facts.to_html(header = False, index = False)

# Write scraped html to file
with open('html_facts_dump.html', 'w+', encoding='utf-8') as f:
    f.write(html_facts)

# Display the HTML table string
print("************")
print("Mars Facts")
print("************")
print(html_facts)


# Mars Hemipheres
def get_html_hemisphere(url_hemisphere, wait):
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(options=fireFoxOptions, executable_path=r"C:/Program Files/Mozilla Firefox/geckodriver.exe")
    driver.get(url_hemisphere)
    driver.implicitly_wait(wait)
    html_hemisphere = driver.page_source
    driver.close()
    return html_hemisphere

url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
html_hemisphere = get_html_hemisphere(url_hemisphere, wait = 5)
soup_hemisphere = bs(html_hemisphere, "html.parser")

# Write scraped html to file
with open('html_hemisphere_dump.html', 'w+', encoding='utf-8') as f:
    f.write(html_hemisphere)

# Retrieve the dictionary of hemispheres
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

print("*******************")
print("Mars Hemispheres ")
print("*******************")    
print(hemisphere_image_urls)


