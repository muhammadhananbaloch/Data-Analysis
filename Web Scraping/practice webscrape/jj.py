import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

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

product_prices = []
for items in complete_items:
    product_prices.append(items.select('div.product-item-info div.product.details.product-item-details div.price-box.price-final_price span.special-price span.price-container.price-final_price.tax.weee span.price-wrapper span.price'))

current_discount = []
for items in complete_items:
    current_discount.append(items.select('div.product-item-info div.product.details.product-item-details div.price-box.price-final_price div.stock.unavailable.discount-percent span'))

product_name=[]
product_id=[]
for names_ids in product_names_id:
    for name_id in names_ids:
        nameAndId = name_id.text.strip()
        head, sep, tail = nameAndId.partition('|')
        product_name.append(head.strip())
        product_id.append(tail.strip())
    
product_price=[]
for prices in product_prices:
    if prices:
        for price in prices:
            product_price.append(price.text.strip('PKR').lstrip())
    else:
        product_price.append('')

discount=[]
for discounts in current_discount:
    if discounts:
        for disc in discounts:
            discount.append(disc.text.strip())
    else:
        discount.append('')

data = {'Product Name': product_name,
        'Product ID': product_id,
        'Price': product_price,
        'Discount': discount}
df = pd.DataFrame(data)

df.to_csv("junaid_jamshed.csv", index=False)