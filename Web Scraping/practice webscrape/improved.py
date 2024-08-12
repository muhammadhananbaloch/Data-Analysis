import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

# load the webpage
base_url = "https://www.junaidjamshed.com/mens/kameez-shalwar.html?p="

product_name=[]
product_id=[]
product_price=[]
discount=[]

page_num=1

while True:
    url=base_url+str(page_num)
    try:
        r = requests.get(url)
        r.raise_for_status()  # Check for request errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_num}: {e}")
        continue
    # convert to a beautiful soup object
    webpage = bs(r.content, "html.parser")

    # Check if there are no more pages to parse
    if not webpage.select('div.page-wrapper'):
        break

    data = webpage.find_all('div', attrs={'class':'product details product-item-details'})
    for item in data:
        try:
            names = item.find('a',{"class": "product-item-link"}).text.strip()
            head, sep, tail = names.partition('|')
            product_name.append(head.strip())
            product_id.append(tail.strip())
        except:
            product_name.append('')
            product_id.append('')


        try:
            product_price.append(item.find('span', attrs={'class':'price'}).text.strip('PKR').lstrip())
        except:
            product_price.append('')

        try:
            discount.append(item.find('div', attrs={'class':'stock unavailable discount-percent'}).text.strip())
        except:
            discount.append('')
            
    next_page = webpage.select('div.page-wrapper main.page-main div.columns div.column.main div.toolbar.toolbar-products div.pages ul.items.pages-items a.action.next')
    print(f"Scrapping page no: {page_num}")
    if next_page:
        page_num +=1
        time.sleep(2)
    else:
        break

pd.DataFrame({'Product Name':product_name, 'Product ID':product_id, 'Product Price':product_price, 'Discount':discount}).to_csv('improved.csv', index=False)