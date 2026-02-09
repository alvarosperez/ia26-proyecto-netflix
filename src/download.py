import os
import json
import requests

from config import ACCESS_TOKEN

url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url_popular_movies, headers=headers)
movies = response.json()["results"]

os.makedirs("data/raw", exist_ok=True)

#Guardar el archivo
file_path = "data/raw/popular_movies.json"

try:
    with open(file_path, "w", encoding="utf-8") as f:
        for movie in movies:
            f.write(json.dumps(movie, ensure_ascii=False) + "\n")

    print(f"Se guardaron {len(movies)} películas en {file_path}")

except Exception as e:
    print(f"Error al guardar el archivo: {e}")

#Genres

url_geners = "https://api.themoviedb.org/3/genre/movie/list"

response = requests.get(url_geners, headers=headers)
genres= response.json()["genres"]

#Guardar el archivo de genre
file_path= "data/raw/movie_genre.json"

with open(file_path, "w", encoding="utf-8") as f:
        for genre in genres:
            f.write(json.dumps(genre) + "\n")

print(f"Se guardaron {len(genres)} géneros en {file_path}")