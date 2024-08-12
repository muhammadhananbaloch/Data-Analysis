import requests
from bs4 import BeautifulSoup as bs

# load the webpage
url = "https://www.junaidjamshed.com/mens/kameez-shalwar.html"
r = requests.get(url)
# convert to a beautiful soup object
webpage = bs(r.content, "html.parser")

page_wrapper = webpage.select('div.page-wrapper')
main = [wrapper.select('main.page-main')for wrapper in page_wrapper]

for columns in main:
    for column in columns:
        complete_items = column.select('div.columns div.column.main div.products.wrapper.grid.products-grid ol li.item.product.product-item')

product_names_id = []
for items in complete_items:
    product_names_id.append(items.select('div.product-item-info div.product.details.product-item-details h2.product.name.product-item-name a'))