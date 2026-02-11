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
    for movie in movies:
        f.write(json.dumps(movie, ensure_ascii=False) + "\n")
    
    ## json.dump(movies, f, indent=4, ensure_ascii=False)

print(f"Se guardaron {len(movies)} películas en {file_path}")
 
## Genres

url_genres = "https://api.themoviedb.org/3/genre/movie/list?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url_genres, headers=headers)
genres = response.json()["genres"]

# Guardar el archivo
file_genres = "data/raw/popular_genres.json"

with open(file_genres, "w", encoding="utf-8") as f:
    for genre in genres:
        f.write(json.dumps(genre, ensure_ascii=False) + "\n")

print(f"Se guardaron {len(genres)} géneros en {file_genres}")


def api_request(url):
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    return response.json()



def data_writing(file_path, data):
    os.makedirs("data/raw", exist_ok=True)

    #Guardar el archivo
    file_path = "data/raw/popular_movies.json"

    with open(file_path, "w", encoding="utf-8") as f:
     for element in data:
        f.write(json.dumps(element, ensure_ascii=False) + "\n")
    
     

# json.dump(movies, f, indent=4, ensure_ascii=False)

    print(f"Se guardaron {len(data)} elementos en {file_path}")
 
    
    
## movies 
    movie_url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    movie_data = api_request(movie_url)
    movie_file_path = "data/raw/popular_movies.json"
    data_writing(movie_file_path, movie_data["results"])


## genres
    genre_url = "https://api.themoviedb.org/3/genre/movie/list?language=en-US"
    genre_data = api_request(genre_url)
    genre_file_path = "data/raw/popular_genres.json"
    data_writing(genre_file_path, genre_data["genres"])