
import os
import requests
import json
from config import ACCESS_TOKEN


def api_request(url):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    return response.json()


def data_writing(file_path, data):

with open(file_path, "w", encoding="utf-8") as f:
    
    for movie in movies:
        f.write(json.dumps(movie) + "\n")
        
    
    #json.dump(movies, f, indent=4, ensure_ascii=False)

print(f"Se gaurdaron {len(movies)} películas en {file_path}")

url_genres = "https://api.themoviedb.org/3/genre/movie/list"

response = requests.get(url_genres, headers=headers)
genres = response.json()["genres"]

#Guardar el archivo
file_path = "data/raw/popular_genres.json"

with open(file_path, "w", encoding="utf-8") as f:
    
    for genre in genres:
        f.write(json.dumps(genres) + "\n")
        

print(f"Se gaurdaron {len(genres)} películas en {file_path}")


def api_request(url):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    # Es buena práctica verificar si la petición fue exitosa
    response.raise_for_status() 
    return response.json()

def data_writing(file_path, data):
    # Aseguramos que la carpeta exista basándonos en la ruta del archivo
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        for element in data:
            # Escribimos en formato JSONL (JSON Lines) como tenías planeado
            f.write(json.dumps(element, ensure_ascii=False) + "\n")
    
    print(f"Se guardaron {len(data)} elementos en: {file_path}")


# 1.  Películas Populares
movie_url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
movie_data = api_request(movie_url)
# Corregido el nombre de la variable 'moviw_file_path' -> 'movie_file_path'
movie_file_path = "data/raw/popular_movies.json"
data_writing(movie_file_path, movie_data["results"])

# 2.  Géneros
genre_url = "https://api.themoviedb.org/3/genre/movie/list?language=en-US"
genre_data = api_request(genre_url)
genre_file_path = "data/raw/movie_genres.json"
# Pasamos los argumentos correctos a la función
data_writing(genre_file_path, genre_data["genres"])

# 3.  Series de TV Populares
# El endpoint para series es /tv/popular
tv_url = "https://api.themoviedb.org/3/tv/popular?language=en-US&page=1"
tv_data = api_request(tv_url)
tv_file_path = "data/raw/popular_series.json"

# Extraemos 'results' porque el JSON que mostraste tiene la misma estructura que las películas
data_writing(tv_file_path, tv_data["results"])

# 4. Procesar Géneros de Series 
tv_genre_url = "https://api.themoviedb.org/3/genre/tv/list?language=en-US"
tv_genre_data = api_request(tv_genre_url)
tv_genre_file_path = "data/raw/tv_genres.json"

data_writing(tv_genre_file_path, tv_genre_data["genres"])