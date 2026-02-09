import requests
import json 
import os 
from config import ACCESS_TOKEN

# SECCIÓN DE INFORMACIÓN Y VARIABLES DE PELÍCULAS POPULARES:
url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
response_movies = requests.get(url_popular_movies, headers=headers)
movies = response_movies.json()["results"]


url_genre_movies = "https://api.themoviedb.org/3/genre/movie/list?language=en"
response_genres = requests.get(url_genre_movies, headers=headers)
genres = response_genres.json()["genres"]


# CÓDIGO IMPRIMIR PELÍCULAS POPULARES Y GÉNEROS:
os.makedirs("data/raw", exist_ok=True)

file_path_movies = "data/raw/popular_movies.json"

with open(file_path_movies, "w", encoding="utf-8") as f:
    for movie in movies:
        f.write(json.dumps(movie) + "\n")

file_path_genres = "data/raw/genre_movies.json"
with open(file_path_genres, "w", encoding = "utf-8") as a:
    for genre in genres:
        a.write(json.dumps(genre) + "\n")

print(f"Se guardaron {len(movies)} películas en {file_path_movies} y {len(genres)} géneros en {file_path_genres}")

