import os
import json
import requests
from logs import registro_log
from config import ACCESS_TOKEN
from clean import json_to_csv

def api_request(url):

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()


def data_writing(file_path, data, mode = "w"):

    os.makedirs("data/raw", exist_ok=True)

    with open(file_path,  mode, encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element) + "\n")

        #print(f"Se guardaron {len(data)} elementos en {file_path}")
        registro_log(f"Se guardaron {len(data)} elementos en {file_path}")

#peliculas
for page in range(1,7):
    movie_url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"
    movie_data = api_request(movie_url)
    movie_file_path = "data/raw/popular_movies.json"
    if page == 1:
        data_writing(movie_file_path, movie_data["results"], mode="w")
    else:
        data_writing(movie_file_path, movie_data["results"], mode="a")


# genres
genre_url = "https://api.themoviedb.org/3/genre/movie/list"
genre_data = api_request(genre_url)
genre_file_path = "data/raw/movie_genres.json" 
data_writing(genre_file_path, genre_data["genres"])

#series
series_url = "https://api.themoviedb.org/3/tv/popular"
series_data = api_request(series_url)
series_file_path = "data/raw/popular_series.json"
data_writing(series_file_path, series_data["results"])

#Generos

generos_url = "https://api.themoviedb.org/3/genre/tv/list"
generos_url = api_request(generos_url)
generos_file_path = "data/raw/series_genre.json"
data_writing(generos_file_path, genre_data["genres"])




    