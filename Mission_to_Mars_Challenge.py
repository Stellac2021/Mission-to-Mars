
#Import Splinter and Beautiful Soup
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

#Optional delat ofr loading the page
browser.is_element_present_by_css('div.list_text', wait_time = 1)


html = browser.html
news_soup = bs(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
paragraph = slide_elem.find('div', class_='article_teaser_body').get_text()
paragraph


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = bs(html, 'html.parser')


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


df.to_html()


# # D1: Scrape High-Resolution Mars' Hemisphere Images and Titles

# ### Hemispheres


# 1. Use browser to visit the URL
url = 'http://marshemispheres.com/'

browser.visit(url)

links = browser.find_by_css("a.product-item img")
links[1]


# 2. Create a list to hold the images and titles
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and tiles for each hemisphere.
links = browser.find_by_css("a.product-item img")

for i in range(len(links)):
    hemisphere = {}

    #For each link click 
    browser.find_by_css("a.product-item img")[i].click()

    #Find the sample image anchor tag and get href
    sample = browser.links.find_by_text("Sample").first
    hemisphere["img_url"] = sample["href"]

    #Find hemisphere title
    hemisphere["title"] = browser.find_by_css("h2.title").text

    #Append image and title to dictionary
    hemisphere_image_urls.append(hemisphere)

    #Navigate back 
    browser.back()

# 4. Print the list that hold the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the brower
browser.quit()

