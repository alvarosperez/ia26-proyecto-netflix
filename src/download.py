import os
import json
import csv
import requests

from logs import registro_logs
from config import ACCESS_TOKEN
from clean import json_to_csv


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


# genres
genre_url = "https://api.themoviedb.org/3/genre/movie/list"
genre_data = api_request(genre_url)
genre_file_path = "data/raw/movie_genres.json"
data_writing(genre_file_path, genre_data["genres"])

# series
serie_url = "https://api.themoviedb.org/3/tv/popular?language=en-US&page=1"
serie_data = api_request(serie_url)
serie_file_path = "data/raw/popular_series.json"
data_writing(serie_file_path, serie_data["results"])

# series genres
serie_genre_url = "https://api.themoviedb.org/3/genre/tv/list?language=en"
serie_genre_data = api_request(serie_genre_url)
serie_genre_file_path = "data/raw/serie_genres.json"
data_writing(serie_genre_file_path, serie_genre_data["genres"])

# movies clean
url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
movies_data = api_request(url_popular_movies)
movies = movies_data["results"]

genre_dict = {genre["id"]: genre["name"] for genre in genre_data["genres"]}

os.makedirs("data/clean", exist_ok=True)
clean_file_path = "data/clean/popular_movies.csv"


with open(clean_file_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "titulo", "generos", "popularidad", "nota"])
    
    for movie in movies:
        movie_id = movie["id"]
        titulo = movie["title"]
        popularidad = movie["popularity"]
        nota = movie["vote_average"]
        generos = [genre_dict[g_id] for g_id in movie["genre_ids"] if g_id in genre_dict]
        generos_str = " | ".join(generos)
        writer.writerow([movie_id, titulo, generos_str, popularidad, nota])