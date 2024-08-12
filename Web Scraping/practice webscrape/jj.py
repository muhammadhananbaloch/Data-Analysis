import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# load the webpage
base_url = "https://www.junaidjamshed.com/mens/kameez-shalwar.html?p="
#complete items
product_names_id = []
product_prices = []
current_discount = []

#scrapped data for data frame
product_name=[]
product_id=[]
product_price=[]
discount=[]
page_num=1
for i in range(1,4):
    url=base_url+str(page_num)
    r = requests.get(url)
    # convert to a beautiful soup object
    webpage = bs(r.content, "html.parser")

    page_wrapper = webpage.select('div.page-wrapper')
    main = [wrapper.select('main.page-main')for wrapper in page_wrapper]

    for columns in main:
        for column in columns:
            complete_items = column.select('div.columns div.column.main div.products.wrapper.grid.products-grid ol li.item.product.product-item')

    for items in complete_items:
        product_names_id.append(items.select('div.product-item-info div.product.details.product-item-details h2.product.name.product-item-name a'))

    for items in complete_items:
        product_prices.append(items.select('div.product-item-info div.product.details.product-item-details div.price-box.price-final_price span.special-price span.price-container.price-final_price.tax.weee span.price-wrapper span.price'))

    for items in complete_items:
        current_discount.append(items.select('div.product-item-info div.product.details.product-item-details div.price-box.price-final_price div.stock.unavailable.discount-percent span'))

    for names_ids in product_names_id:
        for name_id in names_ids:
            nameAndId = name_id.text.strip()
            head, sep, tail = nameAndId.partition('|')
            product_name.append(head.strip())
            product_id.append(tail.strip())
        
    for prices in product_prices:
        if prices:
            for price in prices:
                product_price.append(price.text.strip('PKR').lstrip())
        else:
            product_price.append('')

    for discounts in current_discount:
        if discounts:
            for disc in discounts:
                discount.append(disc.text.strip())
        else:
            discount.append('')
    
    next_page = webpage.select('div.page-wrapper main.page-main div.columns div.column.main div.toolbar.toolbar-products div.pages ul.items.pages-items a.action.next')
    print(f"Scrapping page no: {page_num}")
    if next_page:
        page_num +=1
    else:
        break

data = {'Product Name': product_name,
        'Product ID': product_id,
        'Price': product_price,
        'Discount': discount}
df = pd.DataFrame(data)

df.to_csv("junaid_jamshed.csv", index=False)