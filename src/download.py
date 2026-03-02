import os
import requests
import json
from config import ACCESS_TOKEN
from logs import registro_logs

def api_request(url):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    return response.json()



def data_writing(file_path, data, mode="w"):

    os.makedirs("data/raw", exist_ok=True)

    with open(file_path, mode, encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element, ensure_ascii=False) + "\n")


    registro_logs(f"Se guardaron {len(data)} elementos en {file_path}")

#peliculas
for page in range(1, 7):
    movie_url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"
    movie_data = api_request(movie_url)
    movie_file_path = "data/raw/popular_movies.json"
    if page == 1:
        data_writing(movie_file_path, movie_data["results"], "w")
    else:
        data_writing(movie_file_path, movie_data["results"], "a")

#generos 
genre_url = "https://api.themoviedb.org/3/genre/movie/list?language=en-US"
genre_data = api_request(genre_url)
genre_file_path = "data/raw/movie_genres.json"
data_writing(genre_file_path, genre_data["genres"])


#series populares
for pages in range(1,7):
    tv_url = f"https://api.themoviedb.org/3/tv/popular?language=en-US&page={pages}"
    tv_data = api_request(tv_url)
    tv_file_path = "data/raw/popular_series.json"
    if pages == 1:
        data_writing(tv_file_path, tv_data["results"], "w")
    else:
        data_writing(tv_file_path, tv_data["results"], "a")

#generos de series
tv_genre_url = "https://api.themoviedb.org/3/genre/tv/list?language=en-US"
tv_genre_data = api_request(tv_genre_url)
tv_genre_file_path = "data/raw/tv_genres.json"
data_writing(tv_genre_file_path, tv_genre_data["genres"])
