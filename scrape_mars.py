from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # news title and paragraph
    news_title, news_para = scrape_redPlanet(browser)

    # function mars facts

    
    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_para": news_para,
        "mars_facts": marsFacts()
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

# Function to scrape red planet
def scrape_redPlanet(browser):
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit https://redplanetscience.com/
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the news_title
    news_title = soup.find('div', class_='content_title').get_text()

    # Get the news_para
    news_para = soup.find('div', class_='article_teaser_body').get_text()

    # # Store data in a dictionary
    # mars_data = {
    #     "news_title": news_title,
    #     "news_para": news_para
    # }

    # Return results
    return news_title, news_para


# Function to scrape JPL Mars Space Images - Featured Image
# https://spaceimages-mars.com/
# Example:
# featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'




# Function to scrape Mars Facts
# https://galaxyfacts-mars.com/
# Scrape HTML table

def marsFacts():
    mars_facts_df = pd.read_html('https://galaxyfacts-mars.com/')[0]

    mars_facts_df.columns=['Description: Mars & Earth', 'Mars', 'Earth']
    mars_facts_df.set_index('Description: Mars & Earth', inplace=True)

    # return results
    return mars_facts_df.to_html(classes='table table-striped')



# Function to scrape Mars Hemispheres
# https://marshemispheres.com/
# Obtain high resolution images
# Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]