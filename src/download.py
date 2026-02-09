import os
import json
import requests

from config import ACCESS_TOKEN

url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
url_genres = "https://api.themoviedb.org/3/genre/movie/list?language=en"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

##Listado Peliculas

response = requests.get(url_popular_movies, headers=headers)
movies = response.json()["results"]

os.makedirs("data/raw", exist_ok=True)

#Guardar el archivo
file_path = "data/raw/popular_movies.json"

with open(file_path, "w", encoding="utf-8") as f:
    for movie in movies:
        f.write(json.dumps(movie) + "\n")

print(f"Se guardaron {len(movies)} películas en {file_path}")

##Generos

response_genre = requests.get(url_genres, headers = headers)
genres = response_genre.json()["genres"]

genres_path = "data/raw/genres.json"

with open(genres_path, "w", encoding="utf-8") as f:
    for genre in genres:
        f.write(json.dumps(genre) + "\n")

print(f"Se guardaron {len(genres)} películas en {genres_path}")
