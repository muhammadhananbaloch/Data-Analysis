import requests
from bs4 import BeautifulSoup as bs

# load the webpage
url = "https://www.junaidjamshed.com/mens/kameez-shalwar.html"
r = requests.get(url)
# convert to a beautiful soup object
webpage = bs(r.content, "html.parser")

page_wrapper = webpage.select('div.page-wrapper')
main = [wrapper.select('main.page-main')for wrapper in page_wrapper]


