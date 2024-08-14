from bs4 import BeautifulSoup
import requests
import pandas as pd



book_title= []
book_price = []
book_rating = []
stock_status = []
page_no = 1
while True:
    base_url = f'https://books.toscrape.com/catalogue/page-{page_no}.html'

    response = requests.get(base_url)   
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')
    if response.status_code != 200:
        print('Failed to load page', page_no)   
        break
    else:
        if not books:
            break
        else:
            print(f'Scraping page: {page_no}')
            for book in books:
                try:
                    book_title.append(book.h3.a['title'])
                except:
                    book_title.append('No title available')
                
                try:
                    book_price.append(book.find('p', class_='price_color').text.strip('Â£'))
                except:
                    book_price.append('Price not available')
                try:
                    book_rating.append(book.p['class'][1])  
                except:
                    book_rating.append('Rating not available')

                try:
                    stock_status.append(book.find('p', class_='instock availability').text.strip())
                except:
                    stock_status.append('Stock status not available')

            next_page = soup.find('li', class_='next')  
            if next_page:
                page_no += 1
            else:
                break


book_data = {"Title": book_title, "Price": book_price, "Rating": book_rating, "Stock Status": stock_status}
pd.DataFrame(book_data).to_csv('books.csv', index=False)
