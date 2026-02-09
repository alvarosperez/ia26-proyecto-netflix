
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

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(movies, f, indent=4, ensure_ascii=False)

print(f"Se guardaron {len(movies)} películas en {file_path}")