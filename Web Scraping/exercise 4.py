import requests
from bs4 import BeautifulSoup as bs
import re

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
i=1
for image in image_links:
    image_url = url + image
    img_data = requests.get(image_url).content
    with open(f'image_name{i}.jpg', 'wb') as handler:
        handler.write(img_data)
    i+=1