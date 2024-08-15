from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

try:
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()


    soup = BeautifulSoup(source.text, 'html.parser')
    print(soup)
except Exception as e:
    print(e)
