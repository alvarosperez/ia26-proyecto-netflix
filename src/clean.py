import json 
import os
import csv
import requests
from config import ACCESS_TOKEN



def api_request(url):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    return response.json()

def data_writing_csv(file_path, data, mode):
    # Defino los encabezados de la lista
    headers = ["ID", "Título", "Lista de Géneros", "Popularidad", "Nota"]
    os.makedirs("data/clean", exist_ok=True) # Aseguro que la dirrección exista, como en el código de download
    with open(file_path, mode=mode, encoding="utf-8", newline="") as f: # Dejo una línea para cada información de cada película, de ahí el ""
        writer = csv.DictWriter(f, fieldnames=headers) #Organizo los datos encontrados dentro de f en un diccionario 
        if mode == "w":
            writer.writeheader() #Escribo los encabezados siempre y cuando me encuentre en modo "w"
        for element in data:
            # Los datos que voy a escribir en cada línea extraidos de la url
            writer.writerow({
                "ID": element.get("id"),
                "Título": element.get("title") or element.get("name"), 
                "Lista de Géneros": element.get("genre_ids"),          
                "Popularidad": element.get("popularity"),              
                "Nota": element.get("vote_average")
            }) #La parte de element.get la hice con IA por qué no sabía cómo extraer los datos de la url de forma ordenada y así incluirlos en las lineas del diccionario

# La parte del código de download...
for pages in range(1, 7):
    movie_url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={pages}"
    movie_data = api_request(movie_url)
    movie_file_path = "data/clean/popular_movies.csv" 
    
    if pages == 1:
        data_writing_csv(movie_file_path, movie_data["results"], "w")
    else:
        data_writing_csv(movie_file_path, movie_data["results"], "a")



