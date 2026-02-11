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


    with open(file_path, "w", encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(data) + "\n")

    print(f"Se guardaron {len(data)} elementos en {file_path}")


# movies
movie_url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
movie_data = api_request(movie_url)
movie_file_path = "data/raw/popular_movies.json"
data_writing(movie_file_path, movie_data["results"]) 

# movie genres
movie_genre_url = "https://api.themoviedb.org/3/genre/movie/list"
genre_data = api_request(movie_genre_url)
genre_file_path = "data/raw/movie_genres.json"
data_writing(genre_file_path, genre_data["genres"])

# series
series_url = "https://api.themoviedb.org/3/tv/popular"
series_data = api_request(series_url)
series_file_path = "data/raw/popular_series.json"
data_writing(series_file_path, series_data["results"])

# series genres
series_genre_url = "https://api.themoviedb.org/3/genre/tv/list"
genre_data = api_request(series_genre_url)
series_genre_file_path = "data/raw/series_genres.json"
data_writing(series_genre_file_path, genre_data["genres"])