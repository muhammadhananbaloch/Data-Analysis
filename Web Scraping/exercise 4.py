import requests
from bs4 import BeautifulSoup as bs
import re
import os

# load the webpage
url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url + "webpage.html")    
# convert to a beautiful soup object
webpage = bs(r.content, "html.parser")

# task 1 - grab all images from webpage

images = webpage.select("div.row div.column img")
# save the images

images_url = [image['src'] for image in images]
image_links = [image for image in images_url]

for image in image_links:
    image_url = url + image
    image_name = os.path.basename(image_url)
    # print(image_name)
    img_data = requests.get(image_url).content
    with open(image_name, 'wb') as handler:
        handler.write(img_data)