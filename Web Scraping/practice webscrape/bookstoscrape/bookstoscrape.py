from bs4 import BeautifulSoup
import requests
import pandas as pd

base_url = 'https://books.toscrape.com/catalogue/page-1.html'

response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')


