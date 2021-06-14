# --------- Dependencies ---------
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import pymongo
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver 
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("http://www.google.com/") 
print (driver.title)
driver.quit() 

# --------- Setup splinter ---------
def init_browser(): 
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser = Browser('chrome', **executable_path, headless=False)

def scrape(): 
    browser = init_browser()

    # --------------------------------------------------
    # Scrape NASA Mars News 
    # --------------------------------------------------

    # URL of page to be scraped
    url = 'https://redplanetscience.com/#'
    browser.visit(url)

    print("NASA Mars News: Scraping in Progress...")

    # HTML Object 
    html_url = browser.html

    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(html_url, 'html.parser')

    # Extract lastest News title text 
    news_title = soup.find('div', class_='content_title').text

    # Extract lastest News paragraph text 
    lastest_story = soup.find('div', class_='article_teaser_body').text

    # Display scrapped news 
    print(news_title)
    print("---------------------------------------------------------")
    print(lastest_story)

    print("NASA Mars News: Scraping Complete!")

    # --------------------------------------------------
    # Scrape JPL Mars Space Images - Featured Image
    # --------------------------------------------------

    # Visit the url for the Featured Space Image site
    jpl_images = 'https://spaceimages-mars.com' 
    browser.visit(jpl_images)

    print("JPL Mars Space Images: Scraping in Progress...")

    # HTML Object
    html_image = browser.html
    image_soup = BeautifulSoup(html_image, "html.parser")

    # Extract featured image from JPL Mars Space 
    featured_image = image_soup.find('img', class_='headerimage fade-in')["src"]

    # Create f-string to print full url for image
    featured_image_url = f"https://spaceimages-mars.com/{featured_image}"

    # Display url of featured image 
    print("JPL Mars Space Featured Image")
    print("---------------------------------------------------------")
    print(featured_image_url)
    
    print("JPL Mars Space Images: Scraping Complete!")

    # --------------------------------------------------
    # Scrape Mars Facts
    # --------------------------------------------------

    # Visit the Mars Facts webpage
    mf_url = 'https://galaxyfacts-mars.com'
    browser.visit(mf_url)

    print("Mars Facts: Scraping in Progress...")

    mf_html = browser.html
    soup = BeautifulSoup(html_image, "html.parser")

    table = pd.read_html(mf_url)
    table 

    mf_df = table[0]
    mf_df

    print("Mars Facts: Scraping Complete!")

    # --------------------------------------------------
    # Scrape Mars Hemispheres
    # --------------------------------------------------

    # Visit the Mars Facts webpage
    mh_url = 'https://marshemispheres.com/'
    browser.visit(mh_url)
    
    print("Mars Hemispheres: Scraping in Progress...")
    
    # HTML Object
    marshem_image = browser.html
    soup = BeautifulSoup(marshem_image, "html.parser")

    # Extract Cerberus
    featured_image = image_soup.find('img', class_='headerimage fade-in')["src"]

    # Create f-string to print full url for image
    featured_image_url = f"https://spaceimages-mars.com/{featured_image}"

    hemis = soup.find_all('div', class_='description')
    print(hemis)

    hemis_full = []

    for i in hemis:
        photo_title = i.find("h3").text
        hemis_image = i.find("a", class_="itemLink product-item")["href"]
        
        browser.visit(mh_url +hemis_image)
        
        image_html = browser.html
        web_info = BeautifulSoup(image_html, "html.parser")
        
        image_url = mh_url + web_info.find("img", class_= "wide-image")["src"]
        
        hemis_full.append({"title" : photo_title, "image_url" : image_url})
        
        
        print("")
        print(photo_title)
        print(image_url)
        print("-------------------------------------------------------")
    
    print("Mars Hemisphere Images: Scraping Complete!")
    
    # --------------------------------------------------
    # Put data into dictionary
    # --------------------------------------------------

    scraped_data = {

    }

    return scraped_data
