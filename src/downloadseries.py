import os
import json
import requests

from config import ACCESS_TOKEN

url_popular_series = "https://api.themoviedb.org/3/tv/popular?language=en-US&page=1"
url_genre_series = "https://api.themoviedb.org/3/genre/tv/list?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"

}


os.makedirs("data/raw", exist_ok= True)

print("Descargando series...")
response_series = requests.get(url_popular_series, headers=headers)
data_series = response_series.json()
lista_series = data_series["results"] 


file_series = "data/raw/series_popular.json"

with open(file_series, "w", encoding="utf-8") as f:
    for serie in lista_series:
        
        f.write(json.dumps(serie) + "\n")

print(f"--> Se guardaron {len(lista_series)} series en {file_series}")



print("Descargando géneros...")
response_generos = requests.get(url_genre_series, headers=headers)
data_generos = response_generos.json()
lista_generos = data_generos["genres"] 


file_generos = "data/raw/series_genres.json"

with open(file_generos, "w", encoding="utf-8") as f:
    for genero in lista_generos:
        f.write(json.dumps(genero) + "\n")


print(f"--> Se guardaron {len(lista_generos)} géneros en {file_generos}")
