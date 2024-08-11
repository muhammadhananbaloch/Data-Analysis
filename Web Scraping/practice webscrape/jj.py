import requests
from bs4 import BeautifulSoup as bs

# load the webpage
url = "https://www.junaidjamshed.com/mens/kameez-shalwar.html"
r = requests.get(url)
# convert to a beautiful soup object
webpage = bs(r.content, "html.parser")

product_names = []
# All_Products = webpage.select("div.products.wrapper.grid.products-grid div.product-item-info")  
Complete_page = webpage.select("div.page-wrapper")
products_section = [products.find('main', attrs={'class': 'page-main'}) for products in Complete_page]
Product_columns = [columns.select("div.columns div.column.main") for columns in products_section]
# product_grid = [grid.find_all("div.products.wrapper.grid.products-grid") for grid in Product_columns]
for grid in Product_columns:
    print(grid.find("ul"))

# print(product_grid)
# for product in All_Products:
    # print(product)    

