from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = 'https://books.toscrape.com/catalogue/page-1.html'

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

book_title= []
book_price = []
book_rating = []
stock_status = []
for book in books:
    try:
        book_title.append(book.h3.a['title'])
    except:
        book_title.append('No title available')
    
    try:
        book_price.append(book.find('p', class_='price_color').text.strip('Â£'))
    except:
        book_price('Price not available')
    try:
        book_rating.append(book.p['class'][1])  
    except:
        book_rating.append('Rating not available')

    try:
        stock_status.append(book.find('p', class_='instock availability').text.strip())
    except:
        stock_status.append('Stock status not available')

