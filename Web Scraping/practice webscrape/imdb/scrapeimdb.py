from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
movie_rank=[]
movie_name=[]
try:
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()


    soup = BeautifulSoup(source.text, 'html.parser')

    top_movies = soup.find_all('li', class_='ipc-metadata-list-summary-item sc-10233bc-0 TwzGn cli-parent')

    for movie in top_movies:
        try:
            head, sep, tail = movie.find('h3', class_='ipc-title__text').text.partition('.')
            movie_rank.append(head.strip())
            movie_name.append(tail.strip())
        except:
            movie_rank.append('')
            movie_name.append('')

except Exception as e:
    print(e)

print(movie_rank)
print(movie_name)
