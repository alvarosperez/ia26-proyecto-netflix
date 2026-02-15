import os
import json
import requests

from config import ACCESS_TOKEN

url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

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

    print(f"Se guardaron {len(data)} elementos en {file_path}")


#movies
movie_url= "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
movie_data = api_request(movie_url)
movie_file_path = "data/raw/popular_movies.json"
data_writing(movie_file_path, movie_data["results"])

#genres
genre_url= "https://api.themoviedb.org/3/genre/movie/list"
genre_data = api_request(genre_url)
genre_file_path = "data/raw/movie_genres.json"
data_writing(genre_file_path, genre_data["genres"] )

#series
serie_url= "https://api.themoviedb.org/3/tv/popular?language=en-US&page=1"
serie_data = api_request(serie_url)
serie_file_path = "data/raw/popular_series.json"
data_writing(serie_file_path, serie_data["results"])

#series genres
serie_genre_url = "https://api.themoviedb.org/3/genre/tv/list?language=en"
serie_genre_data = api_request(serie_genre_url)
serie_genre_file_path = "data/raw/serie_genres.json"
data_writing(serie_genre_file_path, serie_genre_data["genres"])

