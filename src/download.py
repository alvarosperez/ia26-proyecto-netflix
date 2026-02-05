
import requests

from config import ACCESS_TOKEN

url_prueba = "https://api.themoviedb.org/3/authentication"
url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url_popular_movies, headers=headers)

print(response.json()["results"])
