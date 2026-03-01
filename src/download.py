import os
import json
import csv
import requests

from config import ACCESS_TOKEN
from logs import registro_logs

url_popular_movies = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

def api_request(url):
    headers = {    
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
     
    response = requests.get(url, headers=headers)
    return response.json()


def data_writing(file_path, data):
     
    os.makedirs("data/raw", exist_ok=True)
    
    with open(file_path, mode, encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element) + "\n")
            
    registro_logs(f"Se guardaron {len(data)} elementos en {file_path}")


#movies
def data_writing(file_path, data, mode= "w"):

    os.makedirs("data/raw", exist_ok=True)

    with open(file_path, mode, encoding="utf-8") as f:
        for element in data:
            f.write(json.dumps(element, ensure_ascii=False) + "\n")
        
        registro_logs(f"Se guardan{len(data)} elementos{file_path}")


#genres
genre_url= "https://api.themoviedb.org/3/genre/movie/list"
genre_data = api_request(genre_url)
genre_file_path = "data/raw/movie_genres.json"
data_writing(genre_file_path, genre_data["genres"] )

#series
serie_url= "https://api.themoviedb.org/3/tv/popular?language=en-US&page=1"
serie_data = api_request(serie_url)
serie_file_path = "data/raw/popular_series.json"
data_writing(serie_file_path, serie_data["results"])

#series genres
serie_genre_url = "https://api.themoviedb.org/3/genre/tv/list?language=en"
serie_genre_data = api_request(serie_genre_url)
serie_genre_file_path = "data/raw/serie_genres.json"
data_writing(serie_genre_file_path, serie_genre_data["genres"])

#movies clean
movies_data = api_request(url_popular_movies)
movies = movies_data["results"]

genre_dict = {genre["id"]: genre["name"] for genre in genre_data["genres"]}

os.makedirs("data/clean", exist_ok=True)

clean_file_path = "data/clean/popular_movies.csv"

with open(clean_file_path, mode="w", encoding="utf-8") as f:
    f.write("id, titulo, generos, popularidad, nota\n")
    
    for movie in movies:
        movie_id = movie["id"]
        titulo = movie["title"]
        popularidad = movie["popularity"]
        nota = movie["vote_average"]
        
        generos = [genre_dict[g_id] for g_id in movie["genre_ids"] if g_id in genre_dict]
        generos_str = ", ".join(generos)
        
        line = f"{movie_id}, {titulo}, {generos_str}, {popularidad}, {nota}\n"
        f.write(line)

registro_logs(f"Archivo limpio creado en {clean_file_path}")