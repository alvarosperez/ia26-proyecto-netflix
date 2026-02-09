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