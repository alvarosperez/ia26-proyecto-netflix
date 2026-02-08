
import requests
import os
import json

from config import ACCESS_TOKEN

url_prueba = "https://api.themoviedb.org/3/authentication"
url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url_popular_movies, headers=headers)

results = response.json()["results"]

os.makedirs("./data/raw", exist_ok=True)

with open("./data/raw/popular_movies.txt", "w") as fIn:
    for movie in results:
        fIn.write(json.dumps(movie) + "\n")

