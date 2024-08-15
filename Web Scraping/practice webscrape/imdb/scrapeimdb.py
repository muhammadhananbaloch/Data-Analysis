from bs4 import BeautifulSoup
import pandas as pd
import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

movie_name=[]
category=[]
title_image=[]
release_year=[]
imdb_rating=[]
rating_vote_count=[]
runtime_minutes=[]
certificate_rating=[]
movie_genre=[]
movie_plot=[]
try:
    source = requests.get('https://www.imdb.com/chart/top/', headers=headers)
    source.raise_for_status()


    soup = BeautifulSoup(source.text, 'html.parser')

    script_tag = soup.find('script', id='__NEXT_DATA__')
    data = json.loads(script_tag.string)
    initial_data_list = (data['props']['pageProps']['pageData']['chartTitles']['edges'])
    for initial_data in initial_data_list:
        try:
            movie_name.append(initial_data.get("node")['titleText']['text'])
        except:
            movie_name.append('')
        
        try:
            category.append(initial_data.get("node")['titleType']['text'])
        except:
            category.append('')

        try:
            title_image.append(initial_data.get("node")['primaryImage']['url'])
        except:
            title_image.append('')

        try:
            release_year.append(initial_data.get("node")['releaseYear']['year'])
        except:
            release_year.append('')
        
        try:
            imdb_rating.append(initial_data.get("node")['ratingsSummary']['aggregateRating'])
        except:
            imdb_rating.append('')
            
        try:
            rating_vote_count.append(initial_data.get("node")['ratingsSummary']['voteCount'])
        except:
            rating_vote_count.append('')

        try:
            runtime_seconds=(initial_data.get("node")['runtime']['seconds'])
            runtime_minutes.append((runtime_seconds/60))
        except:
            runtime_minutes.append('')
        
        try:
            certificate_rating.append(initial_data.get("node")['certificate']['rating'])
        except:
            certificate_rating.append('')
        
        try:
            movie_genre.append([genre['genre']['text'] for genre in (initial_data.get("node")['titleGenres']['genres'])])
        except:
            movie_genre.append('')
        
        try:
            movie_plot.append(initial_data.get("node")['plot']['plotText']['plainText'])
        except:
            movie_plot.append('')

        # for [node] dict_keys(['id', 'titleText', 'titleType', 'originalTitleText', 'primaryImage', 'releaseYear', 'ratingsSummary', 'runtime', 'certificate', 'canRate', 'titleGenres', 'canHaveEpisodes', 'plot', 'latestTrailer', 'series', '__typename'])
except Exception as e:
    print(e)

top_250_movies = {"Movie Title": movie_name,
                "Category": category,
                "Release Year": release_year,
                "IMDB Rating": imdb_rating,
                "Rating Vote Count": rating_vote_count,
                "Runtime Minutes": runtime_minutes,
                "Rated": certificate_rating,
                "Movie Genre": movie_genre,
                "Movie Plot": movie_plot,
                "Title Image": title_image}

pd.DataFrame(top_250_movies).to_csv('top_250_movies.csv', index=False)
