import os
import json
import requests

from config import ACCESS_TOKEN

def api_request(url):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    return response.json()


def data_writing(file_path, data):
   
    os.makedirs("data/raw", exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element) + "\n")

    print(f"Se guardaron {len(data)} películas en {file_path}")


##Peliculas
url_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
movie_data = api_request(url_movies)
movie_path = "data/raw/popular_movies.json"
data_writing(movie_path, movie_data["results"]) 

##Genres
url_genres = "https://api.themoviedb.org/3/genre/movie/list?language=en"
genre_data = api_request(url_genres)
genres_path = "data/raw/genres.json"
data_writing(genres_path, genre_data["genres"])   

##Series
url_series = "https://api.themoviedb.org/3/tv/popular"
series_data = api_request(url_series)
series_path = "data/raw/popular_series.json"
data_writing(series_path, series_data["results"])

##Generes

url_genres_series = "https://api.themoviedb.org/3/genre/tv/list"
genre_series_data = api_request(url_genres_series)
genres_series_path = "data/raw/series_genre.json"
data_writing(genres_series_path, genre_series_data["genres"])